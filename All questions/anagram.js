var isAnagram = function (s, t) {
  let sorted1 = s.split("").sort().join(""); //sorts all alphanumerical and chars, space included
  let sorted2 = t.split("").sort().join("");
  return sorted1 === sorted2 ? true : false;
};
// silent and listen are anagrams
let str = "bana@*$na153";
let str2 = "b5ana@*$na13";

console.log(isAnagram(str, str2));
