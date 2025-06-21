# Git-Set-Up-With-SSH
- [🔐 Step 1: SSH Key তৈরি করা](#-step-1-ssh-key-তৈরি-করা-if-not-already)
- [📋 Step 2: Public key](#-step-2-public-key)
- [🧪 Step 3: GitLab SSH connection test](#-step-3-gitlab-ssh-connection-test)
- [Why ed25519 instead of RSA 2048 bit](#-why-ed25519-)

## 🔐 Step 1: SSH Key তৈরি করা (if not already)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
## 📋 Step 2: Public key 

```bash
cat ~/.ssh/id_ed25519.pub
```

এই key টি Github, GitLab-এ add করতে হবে।

## 🧪 Step 3: GitLab SSH connection test

```bash
ssh -T git@gitlab.com
```

`Output`:`Welcome to GitLab, @your-username!`

 
## 🔐 Why ed25519 ?

🔐 What is Ed25519?
Ed25519 is a public-key digital signature algorithm. It's designed to be:

Fast

Secure

Lightweight (small key and signature size)

Resistant to side-channel attacks

It’s based on the elliptic curve called Curve25519, which is known for both performance and security.

🧠 Key Features of Ed25519
Feature	Description
🔒 Security	128-bit security (modern and strong)
⚡ Speed	Faster than RSA/DSA for both signing and verifying
📦 Size	Smaller keys and signatures
🔁 Deterministic	Same message → same signature every time
✅ Simple	Easy to implement and analyze safely

📦 Key and Signature Sizes
Public Key: 32 bytes

Private Key: 64 bytes (combination of secret + public)

Signature: 64 bytes

🔧 Where Is Ed25519 Used?
SSH authentication (like ssh-keygen)

GitHub/GitLab SSH keys

TLS, VPNs (e.g., WireGuard)

Secure messaging apps (e.g., Signal)

Cryptocurrencies (e.g., Monero, Tezos)

🆚 Ed25519 vs RSA (2048-bit)
Property	RSA (2048-bit)	Ed25519
Key Size	~256 bytes	32–64 bytes
Signature Size	~256 bytes	64 bytes
Security	~112-bit equivalent	128-bit
Speed	Slower	Much faster
Implementation	Complex	Simple & safer


```
git log --oneline --graph --decorate --all
```

