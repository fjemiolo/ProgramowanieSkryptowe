'use strict'

var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

describe('The sum() function', function() {
 it('Returns 4 for 2+2', function() {
   expect(sum(2,2)).to.equal(4);
 });
 it('Returns 0 for -2+2', function() {
   expect(sum(-2,2)).to.equal(0);
 });
});


var total = 0

function cyfry(napis) {
    var nums = napis.replace(/[^0-9]/g, '') /* wszystkie cyfry g - global */
    nums = nums.split('') /* splituje te cyfry */
    
    if (nums.length == 0)
        return 0

    var i = 0;
    var sum = 0;
    while (i < nums.length) {
        sum += parseInt(nums[i]);
        i++;
    }

    if (isNaN(sum)) {
        return 0
    } else {
        return sum
    }
}

function litery(napis) {
    napis = napis.replace(/[0-9]/g, '');
    return napis.length;
}

function suma(napis) {
    var nn = parseInt(napis) /* parsuje każdy znak na string i zwraca pierwszy int lub NaN */
    if (!isNaN(nn))
        total += nn
    return total
}


var data = ''
while (true) {
    data = window.prompt('Podaj dane: ')

    if (data == null)
        break

    console.log('\t' + cyfry(data) + '\t' + litery(data) + '\t' + suma(data))
}

describe("funkcje script2.js", function() {
    total = 0

    //111 -> 3 0 111
    it("cyfry_sameCyfry", function() {
        expect(cyfry('111')).to.equal(3)
    })
    it("litery_sameCyfry", function() {
        expect(litery('111')).to.equal(0)
    })
    it("suma_sameCyfry", function() {
        expect(suma('111')).to.equal(111)
    })

    //aa -> 0 2 111
    it("cyfry_sameLitery", function() {
        expect(cyfry('aa')).to.equal(0)
    })
    it("litery_sameLitery", function() {
        expect(litery('aa')).to.equal(2)
    })
    it("suma_sameLitery", function() {
        expect(suma('aa')).to.equal(111)
    })

    //aa11 -> 2 2 111
    it("cyfry_literyCyfry", function() {
        expect(cyfry('aa11')).to.equal(2)
    })
    it("litery_literyCyfry", function() {
        expect(litery('aa11')).to.equal(2)
    })
    it("suma_literyCyfry", function() {
        expect(suma('aa11')).to.equal(111)
    })

    //11aa -> 2 2 122
    it("cyfry_cyfryLitery", function() {
        expect(cyfry('11aa')).to.equal(2)
    })
    it("litery_cyfryLitery", function() {
        expect(litery('11aa')).to.equal(2)
    })
    it("suma_cyfryLitery", function() {
        expect(suma('11aa')).to.equal(122)
    })

    // -> 0 0 122
    it("cyfry_pustyNapis", function() {
        expect(cyfry('')).to.equal(0)
    })
    it("litery_pustyNapis", function() {
        expect(litery('')).to.equal(0)
    })
    it("suma_pustyNapis", function() {
        expect(suma('')).to.equal(122)
    })
})