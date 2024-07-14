export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = newName;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = newLength;
  }

  set students(newStudents) {
    if (
      !Array.isArray(newStudents)
      || newStudents.some((student) => typeof student !== 'string')
    ) {
      throw TypeError('Students must be an array of string');
    }
    this._students = newStudents;
  }
}
