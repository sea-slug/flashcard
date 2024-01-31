import discord
import argparse
import yaml
import re
import random

HELP_TEXT = ""
client = discord.Client(intents=discord.Intents.all())

# 起動時に発生するイベントハンドラ
@client.event
async def on_ready():
    print("起動")

# メッセージが送信された時に発生するイベントハンドラ
@client.event
async def on_message(message):
    # 発言するチャンネルの指定
    channel = message.channel
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    mentioned_ids = [m.id for m in message.mentions]
    if client.user in message.mentions:
        words = re.sub(r"<@.+>", "", message.content).split()
        if not words:
            return
        if words[0].startswith("-"):
            if words[0] in ["-h", "--help"]:
                help_text = get_help_message(client.user.name)
                await channel.send(help_text)
            elif words[0] in ["-r"]:
                text = rand(vocab)
                await channel.send(text)
        elif len(words) == 1 and words[0] == "rand":
            text = rand(vocab)
            await channel.send(text)
        else:
            # 辞書選択（標準or逆）
            for w in words:
                if w in vocab.keys():
                    dic = vocab
                    break
                elif w in vocab.values():
                    dic = rev_vocab
                    break
            else:
                dic = vocab
            # 変換
            converted_words = [dic.get(w, 'NOT_FOUND') for w in words]
            text = " ".join(converted_words)
            await channel.send(text)
    return

def rand(vocab):
    k, v = random.choice(list(vocab.items()))
    text = f"{k}: ||{v.center(10)}||"
    return text

def get_help_message(username):
    text = "本botの使い方\n"\
        f"`@{username} [変換したい単語] ([変換したい単語2]...)\n"\
        "変換したい単語を上記の通り入力してください．\n"\
        f"> `@{username} rand`または`@{username} -r`でランダムに単語を表示させることもできます"
    return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    parser.add_argument("-r", '--reverse', action='store_true')
    args = parser.parse_args()
    
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    # データ読み込み
    vocab = {}
    delimiter = ","
    for datafile in reversed(config["datafile"]):
        with open(datafile, "r") as f:
            for line in f:
                k, v, *_ = line.split(delimiter)
                k = k.strip()
                v = v.strip()
                if args.reverse:
                    vocab[v] = k
                else:
                    vocab[k] = v
    rev_vocab = {v:k for k, v in vocab.items()}
 
    #Botの起動とDiscordサーバーへの接続
    client.run(config["token"])