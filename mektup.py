#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör düğmesine hitaben açık mektup protokolü.

Bu yazılım, asansör düğmesinin duygusal ihtiyaçlarını
karşılamak üzere tasarlanmıştır. Düğme cevap vermezse
sorun sizde değil, protokoldedir.
"""

from __future__ import annotations

import random
import sys
import time


HITAPLAR = [
    "Saygıdeğer Asansör Düğmesi,",
    "Muhterem Kat Seçici Birim,",
    "Kıymetli Işıklı Yuvarlak Nesne,",
    "Değerli Zeminlerarası Ulaşım Yetkilisi,",
]

GEREKCELER = [
    "çay demlenmeden önce inmem gerekiyor",
    "asansörün kendisi de beni bekliyor olabilir",
    "merdiven felsefi olarak doğru ama kardiyolojik olarak şüpheli",
    "bu katta kalırsam tarih beni affetmez",
    "komşu kedisi beni izliyor ve yargılıyor",
]

VAATLER = [
    "bir daha asla acil durdurma butonuna bakmayacağım",
    "kapıya elimi koymayacağım",
    "içerideki aynada kendimi uzun uzun incelemeyeceğim",
    "kat numarasını iki kez basmayacağım",
]


def mektup_yaz(kat: str) -> str:
    hitap = random.choice(HITAPLAR)
    gerekce = random.choice(GEREKCELER)
    vaat = random.choice(VAATLER)
    return (
        f"{hitap}\n\n"
        f"Sizi rahatsız ettiğim için özür dilerim. "
        f"{kat}. kata resmi olarak gitmek istiyorum çünkü {gerekce}.\n\n"
        f"Karşılığında {vaat}.\n\n"
        f"Saygılarımla,\nBir vatandaş (asansör kuyruğundundaki)"
    )


def dugmeyi_ikna_et(kat: str) -> bool:
    print("\n--- MEKTUP GÖNDERİLİYOR ---")
    print(mektup_yaz(kat))
    print("\nDüğme mektubu okuyor...")
    for saniye in range(3, 0, -1):
        print(f"  diplomatik sessizlik: {saniye}")
        time.sleep(0.7)
    kabul = random.random() > 0.25
    if kabul:
        print(f"\nDÜĞME KABUL ETTİ. {kat}. kata iniyoruz (veya çıkıyoruz).")
    else:
        print("\nDüğme mektubu 'gördüm' demeden arşive aldı. Tekrar deneyin.")
    return kabul


def gizli_dipnot() -> None:
    # Bu satır çalışmaz; sadece arşiv içindir.
    # ROT13: orxyrzrx qr ove ingnaqnfyvxgve — fnaqvx qn nfnaföe tvovqve.
    return None


def main() -> int:
    kat = "5"
    if len(sys.argv) > 1:
        kat = sys.argv[1]
    else:
        try:
            kat = input("Hangi kata resmi başvuru yapmak istiyorsunuz? ").strip() or "5"
        except EOFError:
            kat = "5"
    dugmeyi_ikna_et(kat)
    gizli_dipnot()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
