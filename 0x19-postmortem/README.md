 On January 15, 2024 (UTC), the outage lasted from 10:00 AM to 12:00 PM.
Impact During the downtime, the WordPress website was unavailable. When visiting the website, users encountered connection issues or prolonged loading times. All users of the website were impacted.
Cause The database server's inability to manage incoming queries was the primary cause of the outage, resulting from server memory exhaustion. 
Timeline At 10:00 AM, the issue was identified when the manager reported that he couldn't get into the WordPress website.
It was thought to be a misconfigured database or a network problem. To identify the root of the problem, steps included looking into database performance metrics and server logs  by monitoring notifications that show a significant use of server resources
Restarting the database server fixed the problem by freeing up memory and improving database queries.
The Cause and Solution
The problem was brought on by an excessive amount of server RAM being used by inefficient database queries and high WordPress site traffic. Users experienced slow performance and connection issues as a result of this creating a bottleneck in the database server.
The database server was restarted to optimize database queries and free up memory to fix the problem. 
Remedial and Preventive Actions
Put in place caching mechanisms: Optimise website performance by configuring server-level caching techniques or caching plugins to lessen server load and enhance site performance in general.
Keep an eye on the server's resources: Install monitoring software to keep an eye on server resources like memory, CPU, and disc consumption to identify and stop similar problems from happening again.
Frequent upkeep: Plan routine maintenance procedures to update software, remove obsolete data, and improve server setups for increased efficiency.
Actions
WordPress themes and plugins were patched to guarantee compatibility and maximize efficiency.
Set up disaster recovery plans and automatic backups to reduce downtime in the future.
Used failover and load-balancing techniques to split up traffic and avoid single points of failure.
To reduce downtime,  personnel were educated  on incident response protocols and elevate critical situations as soon as possible.



