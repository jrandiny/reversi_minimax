# Reversi Minimax

Ini adalah program permainan reversi atau yang kadang disebut juga othello

## Menjalankan

Untuk menjalankan siapkan environment dengan menjalankan perintah berikut

```bash
conda create -f env.yml 
```

Setelah itu jalankan kode dengan perintah berikut

```bash
python reversi.py
```

## Opsi

Aplikasi mempunyai beberapa opsi seperti berikut

```
python reversi.py --help

usage: reversi.py [-h] [--benchmark [N]] [--white [WHITE]] [--black [BLACK]]
                  [--gui] [--level [N]]

Reversi game

optional arguments:
  -h, --help       show this help message and exit
  --benchmark [N]  Run in benchmark mode N times (default: 50)
  --white [WHITE]  Specify White AI
  --black [BLACK]  Specify Black AI
  --gui            Using GUI?
  --level [N]      Determine bot level (default: 1)
```