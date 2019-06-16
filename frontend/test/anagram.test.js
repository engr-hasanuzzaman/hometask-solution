var assert = require('assert');
var isAnagram = require('../anagram/index')

describe('isAnagram', function() {
  it('should return true for strings car and rca', function() {
    assert.equal(isAnagram("car", "rca"), true);
  });

  it('should return false for strings foo and bar', function() {
    assert.equal(isAnagram("foo", "bar"), false);
  });

  it('should return true for strings Care and Race', function() {
    assert.equal(isAnagram("Care", "Race"), true);
  });

  it('should return true for strings hasan@test and @testhasan', function() {
    assert.equal(isAnagram("hasan@test", "@testhasan"), true);
  });

  it('should return false for interge 404 and string "anagram"', function() {
    assert.equal(isAnagram(404, "anagram"), false);
  });

  it('should return false for passing no parameter', function() {
    assert.equal(isAnagram(), false);
  });

  it('should return false for passing single parameter', function() {
    assert.equal(isAnagram("foo"), false);
  });

  it('should return true for string "THis is Anagram" and "Ana gram this is"', function() {
    assert.equal(isAnagram("THis is Anagram", "Ana gram this is"), true);
  });

  it('should return true for string this-is-anagram and is-this-anagram', function() {
    assert.equal(isAnagram("this-is-anagram", "is-this-anagram"), true);
  });

  it('should return true for unicode string হাসান and নহাসা', function() {
    assert.equal(isAnagram("হাসান", "নহাসা"), true);
  });

  it('should return true for string 404500 and 544000', function() {
    assert.equal(isAnagram("404500", "544000"), true);
  });
});
