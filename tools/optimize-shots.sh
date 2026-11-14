#!/bin/zsh
# Convierte las capturas del simulador (PNG de 1320 × 2868) en las imágenes del sitio (AVIF y WebP).
# Uso: tools/optimize-shots.sh <carpeta con es/ y en/>
# Necesita ImageMagick, avifenc (libavif) y cwebp.
set -euo pipefail
src="${1:?carpeta con las capturas}"
cd "$(dirname "$0")/.."
tmp="$(mktemp -d)"
convert_one() { # origen destino ancho
  magick "$1" -resize "${3}x" -strip "$tmp/x.png"
  avifenc -q 62 -s 4 "$tmp/x.png" "$2.avif" > /dev/null
  cwebp -quiet -q 80 "$tmp/x.png" -o "$2.webp"
}
for lang in es en; do
  out="assets/img/$lang"
  mkdir -p "$out"
  for name in capture fatigue fatigue-chart plan summary workout live; do
    convert_one "$src/$lang/$name.png" "$out/$name" 720
  done
  convert_one "$src/$lang/today.png" "$out/theme-dark" 480
  for theme in ember light clean solarized contrast; do
    convert_one "$src/$lang/theme-$theme.png" "$out/theme-$theme" 480
  done
done
rm -rf "$tmp"
du -sh assets/img
