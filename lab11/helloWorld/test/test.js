//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var assert = require('assert');
var fs = require('fs');
var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('GET /', function () {
  it('respond with html', function (done) {
    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });
});

describe('Check data.json', function () {
  it('is a json file', function (done) {
    expect('./data.json').to.be.a.jsonFile();
    done()
  });

  it('contains at least one element matching schema', function (done) {
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 5,
      "y": 4,
      "op": "+"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 50,
      "y": 4,
      "op": "+"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 5,
      "y": 4,
      "op": "-"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 50,
      "y": 4,
      "op": "-"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 5,
      "y": 4,
      "op": "*"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 50,
      "y": 4,
      "op": "*"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 5,
      "y": 4,
      "op": "/"
    })
    expect('./data.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 50,
      "y": 4,
      "op": "/"
    })
    done()

  })
})

describe('GET /json/:name (using data.json)', function () {
  it('respond with html', function (done) {
    server
      .get('/json/data.json')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('contain correct value for all operations', function (done) {
    server
      .get('/json/data.json')
      .expect('Content-Type', /html/)
      .expect(200)
      .expect((res) => {
        var match = res.text.match(/(?<=<tr>).*?(?=<\/tr>)/gm)
        for (line of match) {
          var lm = line.match(/(?<=<td>).*?(?=<\/td>)/gm)
          if (lm !== null) {
            assert.equal(eval(lm[0] + lm[1] + lm[2]), lm[3])
          }
        }
      })
      .end(done)
  })
})