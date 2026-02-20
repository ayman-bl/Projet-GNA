# Étude et Comparaison des Générateurs de Nombres Aléatoires

**Auteurs :** BELASRI Ayman, AZIRAR Achraf, OURRAIS Youssef

## Description
Implémentation, évaluation statistique et étude des vulnérabilités de plusieurs générateurs pseudo-aléatoires (PRNG) et cryptographiques (DRBG). Ce projet illustre la différence entre le hasard destiné à la simulation et celui exigé par la cybersécurité.

## Structure
* **` attacks/`** : Preuves de concept des vulnérabilités (prédiction de l'état du LCG, attaque par XOR sur AES-CTR).
* **` generators/`** : Implémentations Python des algorithmes étudiés (LCG, MT19937, BBS, HMAC_DRBG, Box-Muller, XOR_NRBG, `os.urandom`).
* **` notebooks/`** : Tests statistiques (Entropie, $\chi^2$, KS, Autocorrélation) détaillés par algorithme, et le bilan central dans **`global_comparison.ipynb`**.