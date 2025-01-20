import { createClient } from 'redis';

const client = createConnection();

client.on('Error', (err) => {
  console.log('Redis client not connected to the server', err);
});
await client.connect();
console.log('Redis client connected to the server');
await client.quit();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, result) => {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  })
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
