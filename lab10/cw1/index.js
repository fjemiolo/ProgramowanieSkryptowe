import { Operation } from './module.js';


console.log(new Operation(parseInt(process.argv[2]), parseInt(process.argv[3])).sum());