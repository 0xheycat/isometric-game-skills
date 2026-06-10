import json

POS = ("single isometric full grass land block tile, top surface fully covered with lush green grass and a few tiny flowers, "
       "thick solid brown soil base underneath, 2:1 isometric view, soft painterly shading, simple clean composition, "
       "isolated on plain flat background, Hay Day mobile farm game art style, cute hand-painted cartoon, game asset, high quality")
NEG = ("diamond gemstone, crystal, jewel, gem, shiny stone, cracked dry soil, desert ground, bare dirt top, "
       "flat top-down texture, seamless repeating pattern, multiple tiles, tilemap grid, scenery, landscape, "
       "realistic photo, 3d render, blurry, low quality, watermark, text, signature, harsh shadows, busy background, "
       "house, props, building, character")

NOTE = ("RESEP D v3 - ISOMETRIC TILE + AUTO TRANSPARAN (MEOWART)\n\n"
        "BARU: node Inspyrenet Rembg dipasang setelah VAE Decode -> output langsung PNG ALPHA transparan.\n\n"
        "WAJIB INSTALL custom node:\n"
        "  ComfyUI Manager -> Install Custom Nodes -> cari 'Inspyrenet Rembg'\n"
        "  (pack: ComfyUI-Inspyrenet-Rembg). Restart ComfyUI.\n"
        "  Kalau node 'Inspyrenet Rembg' merah = belum keinstall.\n\n"
        "ALTERNATIF (kalau mau pakai yang sudah kamu punya):\n"
        "  - Pack 'ComfyUI-RMBG' (node RMBG), atau\n"
        "  - SAM (sam_vit_b) untuk masking manual.\n"
        "  Tinggal ganti node rembg ini dengan node remove-background pilihanmu,\n"
        "  sambungkan IMAGE dari VAE Decode -> node bg removal -> Save Image.\n\n"
        "GANTI JENIS TILE: ubah frasa permukaan di CLIP positive (lihat daftar set tile di panduan Notion, Bagian 11).\n"
        "Seed FIXED biar bentuk/sudut diamond konsisten antar semua tile.")

nodes = []
nodes.append({"id":1,"type":"CheckpointLoaderSimple","pos":[40,200],"size":[330,98],"flags":{},"order":0,"mode":0,
  "inputs":[],
  "outputs":[{"name":"MODEL","type":"MODEL","links":[1],"slot_index":0},{"name":"CLIP","type":"CLIP","links":[2],"slot_index":1},{"name":"VAE","type":"VAE","links":[],"slot_index":2}],
  "properties":{"Node name for S&R":"CheckpointLoaderSimple"},"widgets_values":["juggernautXL_ragnarokBy.safetensors"]})
nodes.append({"id":2,"type":"LoraLoader","pos":[410,120],"size":[330,126],"flags":{},"order":1,"mode":0,
  "inputs":[{"name":"model","type":"MODEL","link":1},{"name":"clip","type":"CLIP","link":2}],
  "outputs":[{"name":"MODEL","type":"MODEL","links":[3],"slot_index":0},{"name":"CLIP","type":"CLIP","links":[4],"slot_index":1}],
  "properties":{"Node name for S&R":"LoraLoader"},"widgets_values":["isometric/isometric_tilemap_xl.safetensors",0.75,0.75]})
nodes.append({"id":3,"type":"LoraLoader","pos":[410,290],"size":[330,126],"flags":{},"order":2,"mode":0,
  "inputs":[{"name":"model","type":"MODEL","link":3},{"name":"clip","type":"CLIP","link":4}],
  "outputs":[{"name":"MODEL","type":"MODEL","links":[5],"slot_index":0},{"name":"CLIP","type":"CLIP","links":[6,7],"slot_index":1}],
  "properties":{"Node name for S&R":"LoraLoader"},"widgets_values":["utility/white_background_sdxl.safetensors",0.7,0.7]})
nodes.append({"id":5,"type":"CLIPTextEncode","pos":[780,60],"size":[440,190],"flags":{},"order":3,"mode":0,
  "inputs":[{"name":"clip","type":"CLIP","link":6}],
  "outputs":[{"name":"CONDITIONING","type":"CONDITIONING","links":[9],"slot_index":0}],
  "properties":{"Node name for S&R":"CLIPTextEncode"},"widgets_values":[POS]})
nodes.append({"id":6,"type":"CLIPTextEncode","pos":[780,280],"size":[440,170],"flags":{},"order":4,"mode":0,
  "inputs":[{"name":"clip","type":"CLIP","link":7}],
  "outputs":[{"name":"CONDITIONING","type":"CONDITIONING","links":[10],"slot_index":0}],
  "properties":{"Node name for S&R":"CLIPTextEncode"},"widgets_values":[NEG]})
nodes.append({"id":7,"type":"EmptyLatentImage","pos":[780,470],"size":[260,106],"flags":{},"order":5,"mode":0,
  "inputs":[],
  "outputs":[{"name":"LATENT","type":"LATENT","links":[11],"slot_index":0}],
  "properties":{"Node name for S&R":"EmptyLatentImage"},"widgets_values":[1024,1024,1]})
nodes.append({"id":8,"type":"KSampler","pos":[1260,200],"size":[300,262],"flags":{},"order":6,"mode":0,
  "inputs":[{"name":"model","type":"MODEL","link":5},{"name":"positive","type":"CONDITIONING","link":9},{"name":"negative","type":"CONDITIONING","link":10},{"name":"latent_image","type":"LATENT","link":11}],
  "outputs":[{"name":"LATENT","type":"LATENT","links":[12],"slot_index":0}],
  "properties":{"Node name for S&R":"KSampler"},"widgets_values":[123456789,"fixed",30,6.5,"dpmpp_2m","karras",1.0]})
nodes.append({"id":9,"type":"VAELoader","pos":[1260,500],"size":[300,58],"flags":{},"order":7,"mode":0,
  "inputs":[],
  "outputs":[{"name":"VAE","type":"VAE","links":[13],"slot_index":0}],
  "properties":{"Node name for S&R":"VAELoader"},"widgets_values":["sdxl_vae.safetensors"]})
nodes.append({"id":10,"type":"VAEDecode","pos":[1600,200],"size":[210,46],"flags":{},"order":8,"mode":0,
  "inputs":[{"name":"samples","type":"LATENT","link":12},{"name":"vae","type":"VAE","link":13}],
  "outputs":[{"name":"IMAGE","type":"IMAGE","links":[14],"slot_index":0}],
  "properties":{"Node name for S&R":"VAEDecode"},"widgets_values":[]})
nodes.append({"id":13,"type":"InspyrenetRembg","pos":[1830,200],"size":[250,80],"flags":{},"order":9,"mode":0,
  "inputs":[{"name":"image","type":"IMAGE","link":14}],
  "outputs":[{"name":"IMAGE","type":"IMAGE","links":[15],"slot_index":0},{"name":"MASK","type":"MASK","links":[],"slot_index":1}],
  "properties":{"Node name for S&R":"InspyrenetRembg"},"widgets_values":["default"]})
nodes.append({"id":11,"type":"SaveImage","pos":[2110,200],"size":[400,420],"flags":{},"order":10,"mode":0,
  "inputs":[{"name":"images","type":"IMAGE","link":15}],
  "outputs":[],
  "properties":{"Node name for S&R":"SaveImage"},"widgets_values":["meowart_iso_tile_transparent"]})
nodes.append({"id":12,"type":"Note","pos":[40,360],"size":[350,380],"flags":{},"order":11,"mode":0,
  "inputs":[],"outputs":[],"properties":{"text":""},"widgets_values":[NOTE]})

links = [[1,1,0,2,0,"MODEL"],[2,1,1,2,1,"CLIP"],[3,2,0,3,0,"MODEL"],[4,2,1,3,1,"CLIP"],[5,3,0,8,0,"MODEL"],[6,3,1,5,0,"CLIP"],[7,3,1,6,0,"CLIP"],[9,5,0,8,1,"CONDITIONING"],[10,6,0,8,2,"CONDITIONING"],[11,7,0,8,3,"LATENT"],[12,8,0,10,0,"LATENT"],[13,9,0,10,1,"VAE"],[14,10,0,13,0,"IMAGE"],[15,13,0,11,0,"IMAGE"]]

wf = {"last_node_id":13,"last_link_id":15,"nodes":nodes,"links":links,"groups":[],"config":{},"extra":{},"version":0.4}
with open("/data/MEOWART_iso_tile_transparent_resepD_v3.json","w",encoding="utf-8") as f:
    json.dump(wf,f,indent=2,ensure_ascii=False)
with open("/data/MEOWART_iso_tile_transparent_resepD_v3.json") as f:
    json.load(f)
print("OK v3 rembg written")
