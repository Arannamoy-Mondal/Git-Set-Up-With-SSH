# Git-Set-Up-With-SSH

## 🔐 Step 1: SSH Key তৈরি করা (if not already)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
## 📋 Step 2: Public key দেখো

```bash
cat ~/.ssh/id_ed25519.pub
```

এই key টি Github, GitLab-এ add করতে হবে।

## 🧪 Step 5: GitLab SSH connection test

```bash
ssh -T git@gitlab.com
```

`Output`:`Welcome to GitLab, @your-username!`

 
## 🔐 Why ed25519 ?

ed25519 হচ্ছে:
এক ধরনের public-key cryptography algorithm যা SSH key তৈরি করতে ব্যবহার হয়।

🔸 এটা হলো:
একটি modern, fast, এবং secure algorithm

Elliptic Curve Cryptography (ECC)-based

RFC 8032 অনুযায়ী বানানো

✅ কেন ed25519 সেরা চয়েস?
বৈশিষ্ট্য	বিস্তারিত
🔐 Security	খুব শক্তিশালী encryption (128-bit security level)
⚡ Speed	অনেক দ্রুত generate হয় ও authentication করে
🪶 Size	Key size ছোট, কিন্তু security বেশি
🚫 Safer than RSA	RSA 2048-bit এর চেয়ে তুলনামূলক বেশি efficient

📊 তুলনা: ed25519 vs rsa
Feature	ed25519	rsa
Algorithm Type	Elliptic Curve	Integer Factorization
Key Size	256-bit	Usually 2048/4096-bit
Security Level	Strong	Depends on key size
Speed	Faster	Slower
Default Since	OpenSSH 6.5 (2014+)	Much older

🛠️ কখন ব্যবহার করবে?
Situation	Recommended Key Type
New SSH key	✅ ed25519
Compatibility with old systems	⚠️ rsa -b 4096

