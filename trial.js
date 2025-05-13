function disemvowel(str) {
  // Regular expression to match vowels (both uppercase and lowercase)
  const vowels = /[aeiouAEIOU]/g;
  // Replace all vowels with an empty string
  str = str.replace(vowels, "");
  // Return the modified string

  return str;
}
