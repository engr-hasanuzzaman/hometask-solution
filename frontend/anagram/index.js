function isAnagram(str1, str2) {
  if (typeof str1 !== 'string' || typeof str1 !== 'string' || str1 == undefined || str2 == undefined) {
    return false
  }

  var processedStr1 = str1.replace(/[^A-Za-z]+/g, '').toLowerCase();
  var processedStr2 = str2.replace(/[^A-Za-z]+/g, '').toLowerCase();

  var charCounts = [];
  var str1Len = processedStr1.length;
  var str2Len = processedStr2.length

  if (str1Len !== str2Len) { return false; }

  for (let i = 0; i < str1Len; i++) {
    let index = processedStr1.charCodeAt(i)-97;
    charCounts[index] = (charCounts[index] || 0) + 1;
  }

  for (let i = 0; i < str2Len; i++) {
    let index = processedStr2.charCodeAt(i)-97;
    
    // if there is no char, return false otherwise dec count
    if (!charCounts[index]) {
       return false; 
    } else { 
      charCounts[index]--; 
    }
  }

  return true;
}

module.exports = isAnagram