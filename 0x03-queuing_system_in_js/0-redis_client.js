import { createClient } from 'redis';

const client = createConnection();

client.on('Error', (err) => {
  console.log('Redis client not connected to the server', err);
});

await client.connect();

console.log('Redis client connected to the server');
await client.quit();
