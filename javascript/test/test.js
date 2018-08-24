var assert = require('assert');
var {problem1} = require('../set1');

describe('Set One', function() {
  describe('Problem I', function() {
    it('should return -1 when the value is not present', function() {
      assert.equal(problem1("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"), "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t");
    });
  });
});