// file modularga biz uzimizning filega yozganimiz un u shuning un ham file modele deyiladi 
/*
const calculate = require('./hisob');

const natija = calculate.kopaytirish(80,20);
console.log("Natija",natija);
console.log("****************");

const natija2 = calculate.qoshish(70,20);
console.log("Natija",natija2);
console.log("****************");

const natija3 = calculate.ayirish(80,20);
console.log("Natija",natija3);
*/

/*
console.log(require("module").wrapper);
*/

/*
const calculate = require('./hisob');
console.log(arguments);
*/


const Account = require("./accounnts");

Account.tellMeAboutClass();
Account.tellMeTime(); 

console.log("================");

const myAccount = new Account("DANNY", 200000, 974554548554);
myAccount.giveMeDetails();

myAccount.makeDeposit(1000000);

// BMW 400000usd

myAccount.withdrawmoney(400000);

myAccount.makeDeposit(200000);
