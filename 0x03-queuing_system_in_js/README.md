# 0x03. Queuing System in JS

## Overview

This project focuses on creating a queuing system using Redis and Node.js. You will learn how to interact with Redis for various operations, manage asynchronous tasks, and build a basic Express app that integrates a Redis server and a queueing system using Kue. Although Kue is deprecated, it is still widely used in the industry and serves as a foundation for understanding modern queuing systems.

---

## Learning Objectives

By the end of this project, you will be able to:

- Run a Redis server on your machine.
- Perform basic operations with the Redis client.
- Integrate Redis with Node.js for basic operations.
- Store and manipulate hash values in Redis.
- Handle asynchronous operations with Redis.
- Use Kue as a queue system to manage tasks.
- Build a basic Express app that interacts with a Redis server.
- Create an Express app that integrates both Redis and a queueing system.

---

## Resources

- [Redis Quick Start](https://redis.io/docs/getting-started/)
- [Redis Client Interface](https://github.com/redis/node-redis)
- [Redis Client for Node.js](https://www.npmjs.com/package/redis)
- [Kue (deprecated but still used in the industry)](https://github.com/Automattic/kue)

---

## Requirements

- **Environment:**
  - Ubuntu 18.04 LTS
  - Node.js 12.x
  - Redis 5.0.7
- **Coding Standards:**
  - All files must end with a new line.
  - File extensions must be `.js`.
  - The project must include a `README.md` file at the root of the folder.


## Topics Covered

1. **Redis Basics:**
   - Setting up and running a Redis server.
   - Performing simple operations with Redis.
   
2. **Redis with Node.js:**
   - Using the Redis client in Node.js.
   - Managing data types, including hash values.

3. **Asynchronous Operations:**
   - Handling async tasks using Redis.

4. **Queue Management:**
   - Implementing a queue system with Kue.

5. **Express Integration:**
   - Building a basic Express application that interacts with Redis.
   - Extending the app to incorporate both Redis and a queue.

---

## Getting Started

1. **Install Redis:**  
   Follow the [Redis Quick Start](https://redis.io/docs/getting-started/) guide to set up Redis on your machine.

2. **Install Node.js and Dependencies:**  
   - Ensure you have Node.js version 12.x installed.
   - Install required dependencies:
     ```bash
     npm install redis kue express
     ```

3. **Run the Application:**  
   - Start the Redis server:
     ```bash
     redis-server
     ```
   - Run your Node.js app:
     ```bash
     node app.js
     ```

---
