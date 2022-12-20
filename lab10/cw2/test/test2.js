let assert = require('assert');
let fss = require('../fs.js');

describe('exists', function () {
    it('file', function () {
        assert.strictEqual(fss.exists('file.txt'), true)
    });
    it('dir', function () {
        assert.strictEqual(fss.exists('..'), true)
    });
    it('none', function () {
        assert.strictEqual(fss.exists('non-existing-path'), false)
    });
});

describe('isDirectory', function () {
    it('file', function () {
        assert.strictEqual(fss.isDirectory('file.txt'), false)
    });
    it('dir', function () {
        assert.strictEqual(fss.isDirectory('..'), true)
    });
    it('none', function () {
        assert.strictEqual(fss.isDirectory('non-existing-path'), false)
    });
});

describe('isFile', function () {
    it('file', function () {
        assert.strictEqual(fss.isFile('file.txt'), true)
    });
    it('dir', function () {
        assert.strictEqual(fss.isFile('..'), false)
    });
    it('none', function () {
        assert.strictEqual(fss.isFile('non-existing-path'), false)
    });
});
