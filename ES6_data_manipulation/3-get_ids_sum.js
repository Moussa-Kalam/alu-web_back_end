export default function getStudentIdsSum(students) {
  return students.reduce(
    (idSum, currentStudent) => idSum + currentStudent.id,
    0,
  );
}
