# Git-Set-Up-With-SSH-For-Authorization And PGP for Verification
## 📑 Table of Contents

- [🔐 Step 1: SSH Key তৈরি করা (if not already)](#-step-1-ssh-key-তৈরি-করা-if-not-already)
- [📋 Step 2: Public Key GitLab/GitHub এ যুক্ত করা](#-step-2-public-key-gitlabgithub-এ-যুক্ত-করা)
- [🧪 Step 3: GitLab SSH Connection Test](#-step-3-gitlab-ssh-connection-test)
- [💡 Why ED25519 Instead of RSA 2048-bit](#-why-ed25519-instead-of-rsa-2048-bit)
- [🛡️ GPG (GNU Privacy Guard) Setup for Verified Commits](#-gpg-key-setup-for-git-commit-signing-beginner-friendly)
  - [🧩 Step 1: Check if GPG is Installed](#-step-1--check-if-gpg-is-installed)
  - [🧠 Step 2: List Existing GPG Keys](#-step-2--list-existing-keys)
  - [⚙️ Step 3: Generate a New GPG Key](#️-step-3--generate-a-new-gpg-key)
  - [🧾 Step 4: Export Public Key (to Upload on GitHub)](#-step-4-export-public-key-to-upload-on-github)
  - [🔧 Step 5: Tell Git Which Key to Use](#-step-5-tell-git-which-key-to-use)
  - [🪄 Step 6: Enable Auto Signing for Commits](#-step-6-enable-auto-signing-for-commits)
  - [📦 Step 7: Ensure OpenPGP Format](#-step-7-ensure-openpgp-format)
  - [🧪 Step 8: Test Your Setup](#-step-8-test-your-setup)


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

# 🔐 GPG Key Setup for Git Commit Signing (Beginner Friendly)

This guide will help you generate and configure a **GPG key** to make your Git commits show as **🟢 Verified** on GitHub.

---

## 🧩 Step 1 — Check if GPG is Installed

```bash
gpg --version
# Output
# gpg (GnuPG) 2.4.3
# libgcrypt 1.10.2

```

## 🧠 Step 2 — List Existing Keys

```bash
gpg --list-secret-keys --keyid-format LONG
```
```bash
# Example Output:

# /home/arannamoy/.gnupg/pubring.kbx
# -----------------------------------
# sec   rsa4096/50457442CF31EE11 2025-10-18 [SC]
#       Key fingerprint = 1234 ABCD EFGH 5678 90AB CDEF 5045 7442 CF31 EE11
# uid   [ultimate] Arannamoy Mondal <arannamoy@example.com>
# ssb   rsa4096/1122AABB3344CCDD 2025-10-18 [E]


# 👉 Copy the long key ID — here it’s 50457442CF31EE11.
```

## ⚙️ Step 3 — Generate a New GPG Key

```bash
time gpg --quick-generate-key
```

## 🧾 Step 4 — Export Public Key (to Upload on GitHub)

```bash
gpg --armor --export arannamoy@example.com
```

👉 Copy this full block and paste it in GitHub → Settings → SSH and GPG keys → New GPG Key.

## 🔧 Step 5 — Tell Git Which Key to Use

```bash
git config --global user.signingkey 50457442CF31EE11
```
👉 Replace with your own key ID.


## 🪄 Step 6 — Sign All Commits Automatically

```bash
git config --global commit.gpgsign true
```

## 📦 Step 7 — Ensure OpenPGP Format

```bash
git config --global gpg.format openpgp
```

### 🧪 Step 8 — Test Your Setup

```bash
git commit -S -m "Verified commit test"
```


> Credits: Certain parts of this documentation were prepared with reference to Mistral AI’s materials.