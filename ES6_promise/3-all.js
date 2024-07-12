import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const { body } = await uploadPhoto();
    const { firstName, lastName } = await createUser();
    console.log(`${body} ${firstName} ${lastName}`);
  } catch (error) {
    console.log('Signup system offline');
  }
}
