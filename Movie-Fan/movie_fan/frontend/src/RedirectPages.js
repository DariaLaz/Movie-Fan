const registerPage = "/register";
const loginPage = "/login";
const gameDetailsPage = (gameId) => `/games/${gameId}`;
const uploadPage = (categoryId) => `/upload/${categoryId}`;
const createGamePage = "/create-game";
const joinPage = "/join";
const homePage = "/";
const votePage = (categoryId) => `/vote/${categoryId}`;

export {
  registerPage,
  loginPage,
  gameDetailsPage,
  uploadPage,
  createGamePage,
  joinPage,
  homePage,
  votePage,
};
