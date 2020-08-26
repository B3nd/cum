require('dotenv').config();
const Discord = require('discord.js');
const bot = new Discord.Client();
const TOKEN = process.env.TOKEN;
const commands = ['!help', '!kiсk <user>', '!hentai', '!brrr', '!love', '!gay']
const orehus = ['/home/stas/Node/Discord/Oreh/orehus.png',
  '/home/stas/Node/Discord/Oreh/chlen_verh.png',
  '/home/stas/Node/Discord/Oreh/chlen_niz.png',
  '/home/stas/Node/Discord/Oreh/partia.png'
]
bot.login(TOKEN);

bot.on('ready', () => {
  console.info(`Logged in as ${bot.user.tag}!`);
});

bot.on('message', msg => {
  if (msg.content === '!help') {
    let commands_text = 'Вот все комманды: '
    for (let i = 0; i < commands.length - 1; i++) {
      commands_text += commands[i] + ', '
    }
    commands_text += commands[commands.length - 1] + ' 💓'
    msg.channel.send(commands_text)
  } else if (msg.content === 'ping') {
    msg.reply('pong');
    //msg.channel.send('pong');

  } else if (msg.content.startsWith('!kick')) {
    if (msg.mentions.users.size) {
      const taggedUser = msg.mentions.users.first();
      msg.channel.send(`${msg.author} kicked ${taggedUser}`);

    } else {
      msg.reply('Please tag a valid user!');
    }
  } else if (msg.content === '!hentai') {
    //msg.channel.send('Чё, не открывается? Иди делом займись!')
    tag = ''
    for(i = 0; i < 6; i++){ 
      number = Math.random() * 10
      number = number + ''
      number = number[0]
      tag = tag + number
    }
    ref = `https://nhentai.net/g/${tag}`
    msg.channel.send(`Here is your hentai 😏`)
    msg.channel.send(ref)
  } else if (msg.content === '!brrr') {
    msg.channel.send('Haha, bot go brrr')
  } else if (msg.content === 'Справедливо') {
    let m = Math.random()
    if (m <= 0.34) {
      msg.channel.send('', {
        files: [orehus[0]]
      })
    } else if (m <= 0.67) {
      msg.channel.send('', {
        files: [orehus[1]]
      })
      msg.channel.send('', {
        files: [orehus[2]]
      })

    } else {
      msg.channel.send('', {
        files: [orehus[3]]
      })
    }
  } else if(msg.content === '!love'){
    msg.channel.send(msg.author + ' ❤️ 🧡 💛 💚 💙 💜')
  } else if(msg.content === '!gay'){
    msg.channel.send(msg.author + ' 🌈🌈🌈')
  } 
});