const { Telegraf } = require("telegraf");
const TOKEN = "5580082490:AAFs1JQZ0iPtTnB8zDjil1E-00yaM64pKPg";
const bot = new Telegraf(TOKEN);

const web_link = "https://preeminent-concha-eb0104.netlify.app";

bot.start((ctx) =>
  ctx.reply("Welcome :)))))", {
    reply_markup: {
      keyboard: [[{ text: "web app", web_app: { url: web_link } }]],
    },
  })
);
bot.launch();