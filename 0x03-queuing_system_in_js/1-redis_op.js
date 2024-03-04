const redis = require('redis');

const client = redis.createClient();

client.on('connect', () => {
    console.log("Redis client connected to the server")
});

client.on('error', (err) => {
    console.error("Redis client not connected to the server: ", err)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function(err, reply) {
        if (err) {
            console.error('Error setting school:', err);
        } else {
            redis.print(`Reply: ${reply}`);
        }
    });
};

function displaySchoolValue(schoolName) {
    client.get(schoolName, function(err, result) {
        if (err) {
            console.error('Error getting school value:', err);
        } else {
            console.log(result);
        }
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');