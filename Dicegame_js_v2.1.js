const { JSDOM } = require("jsdom");
const { window } = new JSDOM()
const eight = 100000000
const mil = 1000000
let what = 0
let stop;


var win = 0
var loss = 0
var capital = 1000*eight;
var basebet = 1;
var chance = 0800;

var done = 0;
var smallestcapital = capital;
var nextbet = basebet;
var previousbet = nextbet;
var basecapital = capital;
var biggestbet=0;
var count = 0;
var chan = chance/100;
var winmulti = 99/chan;
console.log(winmulti);


function playGame(){
    for (let index = 0; index <= 10000; index++) {

        var test_data = generateDataset(1,10000,mil);
        for (let i of test_data) {
            if (i < chance) {
                capital +=(winmulti*nextbet)-nextbet;
                win +=1;
                winn = 1;
                nextbet=basebet;
            }
            else {
                capital -=nextbet;
                nextbet=previousbet*1.12;
                winn = 0;
                loss +=1;
                if (capital<0 || nextbet>capital){
                    console.log("\nDONE!!!\n");
                    done +=1
                    return 0
                }
            }
            if (nextbet < 0) {
                nextbet=basebet;
            }
            if (capital>basecapital*2 && what!=1) {
                stop = window.performance.now();
                what = 1;
            }
            if (nextbet > biggestbet) {
                biggestbet=nextbet;
            }
            if (capital < smallestcapital) {
                smallestcapital=capital;
            }
            if (count % mil == 0){
                console.log("I: %d\t Chance: %d\t bet: %d  \t Win?: %d \t Capital %d\t BiggestBet: %d \t countM: %d \t SC: %d", i,chance, previousbet,winn,capital/eight,biggestbet/eight,count/1000000, smallestcapital/eight);
            }

            count += 1
            previousbet = nextbet;
        }
    }
    return 1;
}

const start = window.performance.now()
playGame();

let t = ((stop - start)/1000);
console.log(`Time Taken to Double = ${(stop - start)/1000} seconds`);
console.log(t, basecapital)
console.log("Burning Rate: %d", (basecapital/t/1000000))

function generateDataset(min,max,size) {
    function rng(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
    }

    var realdata = [];

    for (let step = 0; step < size; step++) {
        realdata.push(rng(min,max));
        
    }

    return realdata;
}
console.log("Capital: %d\nWinLoss: %d;%d   Death %d", capital,win,loss,done);
