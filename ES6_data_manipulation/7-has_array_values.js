export default function hasValuesFromArray(set, array) {
  let result = true;
  for (const value of array) {
    if (!set.has(value)) result = false;
  }
  return result;
}
