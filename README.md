# MockPokemonGOMap

Further thoughts and questions regarding the project

T - Thoughts

Q - Questions

A - Answers

* Q: What does query server cluster do? What does crawler server cluster do?

* A: Query servers will call Google S2 service and break the four coordinates passed in from frontend into an array of level 15 cell ids. Then it will put the cell ids into the Queue and pull Pokemon ids corresponding to each cell id from the DB.

  Crawler servers will pull cell ids from the Queue, pass cell ids to (mock) Pokemon API, parse the return result and write Pokemon ids into the DB.

* Q: Why do you separate the query service and the crawler service?

* A: The traffic flow into the query service and the crawler service are not the same (see below for the reason). By separating them out, we can take advantage of AWS Elastic Beanstalk and scale up and down our program in a more flexible way. Also, the two services are connected through SQS which is async. So the query services will not be blocked by the slower crawling function.

* Q: How does frontend getting Pokemon info from the backend?

* A: Frontend will send query request every 1 sec and wait for the result in JSON format returned by Query servers.

* Q: So the frontend is pulling. Why do you make query and crawler asynchronous, but frontend synchronous?

* A: I can't improve the logic of frontend because currently, I can't predict the refresh rate of Pokemon. If I know when new Pokemon will show up in each cell, I could make the backend start crawling itself and push the result into the frontend, instead of frontend actively triggering the start of the crawlers.

* T: Move "needs_to_crawl" logic from crawl server cluster to query server cluster.

* A: Moving the checking duplicate cell id within certain time frame logic into the query server cluster will reduce the messages dumped into the Queue.

* T: Totally replace DB with Redis.

* A: Since the information we saved into DB is not crucial at all and I am crawling those data every half minute, I don't really need a DB. I can just use Redis for saving and pulling Pokemon ids.

* Q: Look like the Crawler servers have higher latency than the Query servers. So do you allocate more machines for the Crawler servers?

* A: Even though the Crawler servers does have higher latency than the Query servers, I might not need more machines for the crawler servers. We have to think the usage scenario of the project: Pokemon go is more popular in certain areas. For example, there might be more people play Pokemon go and querying the Pokemon in New York central park than the whole Oklahoma state. So there might be large traffic coming into the query servers with duplicated cell ids. Since the "needs_to_crawl" logic will be moved into the query servers and only unique cell ids will be dumped into the Queue and processed by the crawler servers, the number of request ratio between coming into the query and the crawler maybe 1000:1 or larger. Of course, that is only my assumption and we have to study the real traffic to make decisions. 
