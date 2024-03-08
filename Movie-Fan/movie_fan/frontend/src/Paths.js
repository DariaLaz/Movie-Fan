const categoryPath = "/api/category/";
const registerPath = "/api/register/";
const gamesPath = "/api/games/";
const playerPath = "/api/players/";
const joinPath = "/api/join/";
const loginPath = "/api/login/";
const moviePath = `/api/movies/`;
const submitionPath = `/api/submition/`;
const sarpPath = "/api/sarp_movie/";
const logoutPath = "/api/logout/";

function getPath(path, obj) {
  var entirePath = [];
  entirePath.push(path);
  if (obj) {
    entirePath.push("?");
    for (const [key, value] of Object.entries(obj)) {
      entirePath.push(`${key}=${value}`);
      entirePath.push(`&`);
    }
    entirePath.pop();
  }
  return entirePath.join("");
}

export {
  categoryPath,
  registerPath,
  gamesPath,
  playerPath,
  joinPath,
  loginPath,
  moviePath,
  submitionPath,
  sarpPath,
  logoutPath,
  getPath,
};
