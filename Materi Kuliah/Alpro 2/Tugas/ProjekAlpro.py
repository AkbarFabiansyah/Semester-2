from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# =========================
# DATABASE
# =========================

conn = sqlite3.connect("saldo.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    uid TEXT PRIMARY KEY,
    nama TEXT,
    saldo INTEGER
)
""")

conn.commit()

# =========================
# REGISTER USER
# =========================

@app.route("/register", methods=["POST"])
def register():

    data = request.json

    uid = data["uid"]
    nama = data["nama"]
    saldo = data["saldo"]

    cur.execute(
        "SELECT * FROM users WHERE uid=?",
        (uid,)
    )

    check = cur.fetchone()

    if check:
        return jsonify({
            "status": "error",
            "message": "User sudah ada"
        })

    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        (uid, nama, saldo)
    )

    conn.commit()

    return jsonify({
        "status": "success",
        "message": "User berhasil ditambahkan"
    })

# =========================
# CEK SALDO
# =========================

@app.route("/saldo/<uid>")
def saldo(uid):

    cur.execute(
        "SELECT * FROM users WHERE uid=?",
        (uid,)
    )

    user = cur.fetchone()

    if user:
        return jsonify({
            "nama": user[1],
            "saldo": user[2]
        })

    return jsonify({
        "status": "error",
        "message": "User tidak ditemukan"
    })

# =========================
# TOP UP
# =========================

@app.route("/topup", methods=["POST"])
def topup():

    data = request.json

    uid = data["uid"]
    jumlah = data["jumlah"]

    cur.execute(
        "SELECT * FROM users WHERE uid=?",
        (uid,)
    )

    user = cur.fetchone()

    if not user:
        return jsonify({
            "status": "error",
            "message": "User tidak ditemukan"
        })

    saldo_baru = user[2] + jumlah

    cur.execute(
        "UPDATE users SET saldo=? WHERE uid=?",
        (saldo_baru, uid)
    )

    conn.commit()

    return jsonify({
        "status": "success",
        "saldo": saldo_baru
    })

# =========================
# PEMBAYARAN
# =========================

@app.route("/bayar", methods=["POST"])
def bayar():

    data = request.json

    uid = data["uid"]
    jumlah = data["jumlah"]

    cur.execute(
        "SELECT * FROM users WHERE uid=?",
        (uid,)
    )

    user = cur.fetchone()

    if not user:
        return jsonify({
            "status": "error",
            "message": "User tidak ditemukan"
        })

    saldo = user[2]

    if saldo < jumlah:
        return jsonify({
            "status": "error",
            "message": "Saldo tidak cukup"
        })

    saldo_baru = saldo - jumlah

    cur.execute(
        "UPDATE users SET saldo=? WHERE uid=?",
        (saldo_baru, uid)
    )

    conn.commit()

    return jsonify({
        "status": "success",
        "saldo": saldo_baru
    })

# =========================
# RUN SERVER
# =========================

app.run(host="0.0.0.0", port=5000)