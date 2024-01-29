const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

class User {
  constructor(username) {
    this.username = username;
    this.ads = [];
    this.favorites = [];
  }

  add_advertise(title, tag) {
    this.ads.push({ title, tag });
  }

  rem_advertise(title) {
    const adIndex = this.ads.findIndex((ad) => ad.title === title);
    this.ads.splice(adIndex, 1);
  }

  list_my_advertises(tag) {
    if (tag)
      console.log(
        this.ads
          .filter((ad) => ad.tag === tag)
          .map((ad) => ad.title)
          .join(" ")
      );
    else console.log(this.ads.map((ad) => ad.title).join(" "));
  }

  is_in_favorites(title) {
    return !!this.favorites.find((favorite) => favorite.title === title);
  }

  add_favorite(title, tag) {
    return this.favorites.push({ title, tag });
  }

  rem_favorite(title) {
    const favoriteAdIndex = this.favorites.findIndex(
      (favoriteAd) => favoriteAd.title === title
    );
    this.favorites.splice(favoriteAdIndex, 1);
  }

  list_favorite_advertises(tag) {
    if (tag)
      console.log(
        this.favorites
          .filter((favorite) => favorite.tag === tag)
          .map((favorite) => favorite.title)
          .join(" ")
      );
    else
      console.log(this.favorites.map((favorite) => favorite.title).join(" "));
  }
}

class Ads {
  constructor(title, username, tag) {
    this.title = title;
    this.user = username;
  }
}

const users = {};
const ads = {};

const commands = {
  register(username) {
    if (users[username]) console.log("invalid username");
    else {
      users[username] = new User(username);
      console.log("registered successfully");
    }
  },
  add_advertise(username, title) {
    if (!users[username]) console.log("invalid username");
    else if (ads[title]) console.log("invalid title");
    else {
      users[username].add_advertise(title);
      ads[title] = new Ads(title, username);
      console.log("posted successfully");
    }
  },
  rem_advertise(username, title) {
    if (!users[username]) console.log("invalid username");
    else if (!ads[title]) console.log("invalid title");
    else if (ads[title].user !== username) console.log("access denied");
    else {
      delete ads[title];
      users[username].rem_advertise(title);
      console.log("removed successfully");
    }
  },
  list_my_advertises(username) {
    if (!users[username]) console.log("invalid username");
    else users[username].list_my_advertises();
  },
  add_favorite(username, title) {
    if (!users[username]) console.log("invalid username");
    else if (!ads[title]) console.log("invalid title");
    else if (users[username].is_in_favorites(title))
      console.log("already favorite");
    else {
      users[username].add_favorite(title);
      console.log("added successfully");
    }
  },
  rem_favorite(username, title) {
    if (!users[username]) console.log("invalid username");
    else if (!ads[title]) console.log("invalid title");
    else if (!users[username].is_in_favorites(title))
      console.log("already not favorite");
    else {
      users[username].rem_favorite(title);
      console.log("removed successfully");
    }
  },
  list_favorite_advertises(username) {
    if (!users[username]) console.log("invalid username");
    else users[username].list_favorite_advertises();
  },
};

rl.question("", (commandCount) => {
  for (let i = 0; i < parseInt(commandCount); i++) {
    rl.question("", (command) => {
      command = command.split(" ");
      command = command.slice(0, 1).concat([command.slice(1)]);
      commands[command[0]](...command[1]);
    });
  }

  // rl.close();
});
