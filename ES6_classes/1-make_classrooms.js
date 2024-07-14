import Classroom from './0-classroom';

export default function initialize() {
  const classRoom1 = new Classroom(19);
  const classRoom2 = new Classroom(20);
  const classRoom3 = new Classroom(34);
  return [classRoom1, classRoom2, classRoom3];
}
