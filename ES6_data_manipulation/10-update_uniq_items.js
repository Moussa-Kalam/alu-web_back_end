export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) throw new Error('Cannot process');
  for (const item of groceries.keys()) {
    if (groceries.get(item) === 1) {
      groceries.set(item, 100);
    }
  }
}
