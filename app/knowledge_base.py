"""
================================================================================
KRISHI BONDO — EXPANDED AGRICULTURAL KNOWLEDGE BASE
================================================================================
Comprehensive crop database with 10 major crops covering cereals, vegetables,
fruits, cash crops, pulses, and oilseeds. Each crop has 13+ sections for
fine-grained RAG retrieval.

Crops covered:
1. Rice         2. Wheat         3. Maize         4. Potato
5. Tomato       6. Onion         7. Mango         8. Banana
9. Cotton       10. Lentil

Data sources synthesized from:
- ICAR (Indian Council of Agricultural Research)
- BARI (Bangladesh Agricultural Research Institute)
- FAO Crop Information
- IRRI, CIP, AVRDC, ICRISAT
================================================================================
"""

KNOWLEDGE_BASE = {

    # ============================================================
    # 1. RICE (Oryza sativa)
    # ============================================================
    "rice": {
        "scientific_name": "Oryza sativa",
        "family": "Poaceae (Grass family)",
        "overview": (
            "Rice is the staple food for over half the world's population and the most "
            "important cereal crop in South and Southeast Asia. It is a semi-aquatic "
            "annual grass that thrives in flooded paddy fields. Global production exceeds "
            "500 million tonnes annually, with India, China, and Bangladesh as top producers."
        ),
        "soil_requirements": (
            "Rice grows best in heavy clay or clay-loam soils with high water retention. "
            "Optimal pH range is 5.5 to 7.0. Soils rich in organic matter (above 1.5%) "
            "produce higher yields. Alluvial soils of river deltas (like the Indo-Gangetic "
            "plain and Bengal delta) are ideal. The soil should be puddled before "
            "transplanting to reduce water percolation and control weeds."
        ),
        "climate_requirements": (
            "Rice requires warm, humid conditions. Optimal temperature is 20°C to 35°C, "
            "with minimum 20°C for germination and 25-30°C for tillering. Annual rainfall "
            "of 1000-2000 mm is ideal. Rice is highly sensitive to cold below 15°C and "
            "heat stress above 38°C, especially during flowering."
        ),
        "growing_season": (
            "In India and Bangladesh: Kharif/Aman (June-November, monsoon-fed), Rabi/Boro "
            "(November-April, irrigated), and Aus (April-July). Crop duration ranges from "
            "90 days (short-duration) to 150 days (long-duration). Transplanting is done "
            "21-30 days after sowing in nurseries."
        ),
        "popular_varieties": (
            "High-yielding varieties: IR-64, Swarna (MTU-7029), BPT-5204 (Samba Mahsuri), "
            "Pusa Basmati 1121, Pusa Basmati 1509, BRRI dhan 28, 29, 89. Hybrid varieties: "
            "PHB-71, KRH-2. Drought-tolerant: Sahbhagi Dhan, BRRI dhan 56. Aromatic: "
            "Basmati 370, Pusa 1718, Kalijira."
        ),
        "water_management": (
            "Rice needs 1200-1500 mm of water per crop cycle. Maintain 2-5 cm standing "
            "water during vegetative stage and 5-10 cm during reproductive stage. Drain "
            "fields 10 days before harvest. Alternate Wetting and Drying (AWD) technique "
            "can save 30% water without yield loss."
        ),
        "fertilizer_recommendation": (
            "Apply NPK at 120:60:60 kg/ha for high-yielding varieties. Nitrogen split: "
            "50% basal, 25% at tillering (25 DAT), 25% at panicle initiation (45 DAT). "
            "Apply 5-10 tonnes of farmyard manure (FYM) per hectare before transplanting. "
            "Zinc deficiency is common—apply 25 kg zinc sulfate/ha if soil tests show low Zn."
        ),
        "common_pests": (
            "1) Brown Planthopper (BPH) — causes 'hopperburn'; control with Imidacloprid "
            "or Buprofezin. 2) Stem Borer — leads to 'deadheart' and 'whitehead'; use "
            "Cartap Hydrochloride. 3) Leaf Folder — folds leaves longitudinally; spray "
            "Chlorantraniliprole. 4) Gall Midge — causes 'silver shoot'; use resistant "
            "varieties like Suraksha."
        ),
        "common_diseases": (
            "1) Blast (Magnaporthe oryzae) — diamond-shaped lesions on leaves; control "
            "with Tricyclazole. 2) Bacterial Leaf Blight (BLB) — yellow stripes drying to "
            "straw color; use copper-based bactericides. 3) Sheath Blight — irregular "
            "spots on leaf sheaths; spray Hexaconazole. 4) Tungro virus — yellow-orange "
            "discoloration; control leafhopper vectors."
        ),
        "harvesting": (
            "Harvest when 80-85% of grains turn golden yellow and grain moisture is "
            "20-25%. Cut crop close to ground, allow field drying for 2-3 days, then "
            "thresh. Use combine harvesters for large fields. Dry grain to 14% moisture "
            "for safe storage."
        ),
        "average_yield": (
            "Traditional varieties: 2-3 tonnes/hectare. High-yielding varieties: 5-7 "
            "tonnes/ha. Hybrid varieties: 7-10 tonnes/ha under optimal management. "
            "World average: 4.6 tonnes/ha; Indian average: 4.0 tonnes/ha; Bangladesh: 4.3 t/ha."
        ),
    },

    # ============================================================
    # 2. WHEAT (Triticum aestivum)
    # ============================================================
    "wheat": {
        "scientific_name": "Triticum aestivum",
        "family": "Poaceae (Grass family)",
        "overview": (
            "Wheat is the world's second-most important cereal crop after rice, providing "
            "20% of global dietary calories and protein. It is a cool-season grass adapted "
            "to temperate climates. India is the second-largest producer globally after "
            "China, with Punjab, Haryana, and Uttar Pradesh as major wheat belts."
        ),
        "soil_requirements": (
            "Wheat thrives in well-drained loam to clay-loam soils with good moisture-"
            "holding capacity. Optimal pH: 6.0 to 7.5. Heavy clay soils need good drainage. "
            "Sandy soils require frequent irrigation. Avoid waterlogged or saline-alkaline "
            "soils. Deep soils (60+ cm) support better root development."
        ),
        "climate_requirements": (
            "Cool-season crop. Optimal temperature: 15-25°C, with cool nights essential "
            "for grain filling. Germination: 4-6°C minimum, 20-25°C optimum. Sensitive to "
            "frost during flowering. Heat stress above 30°C during grain filling reduces "
            "yields significantly. Requires 500-700 mm well-distributed rainfall."
        ),
        "growing_season": (
            "Rabi crop in India: sowing November-December, harvest March-April. Timely "
            "sowing (November 1-25) gives highest yields. Late sowing (after December 15) "
            "reduces yields by 25-40 kg/ha/day. Crop duration: 120-150 days."
        ),
        "popular_varieties": (
            "HD-2967 (most widely grown), HD-3086, HD-3226 (heat-tolerant), DBW-187, "
            "DBW-222, PBW-725, WH-1105. Durum wheat: HI-8759, MPO-1215. Bangladesh: "
            "BARI Gom 28, 29, 30, 33 (heat-tolerant), Bijoy."
        ),
        "seed_preparation": (
            "Seed rate: 100-125 kg/hectare for timely sowing; 125-150 kg/ha for late "
            "sowing. Treat seeds with Carbendazim (2.5 g/kg) or Vitavax (1.5 g/kg) to "
            "prevent loose smut and seed-borne diseases. Inoculate with Azotobacter and "
            "PSB biofertilizers for better nitrogen and phosphorus uptake."
        ),
        "sowing_method": (
            "Use seed drill for line sowing at 22.5 cm row spacing. Sowing depth: 5-6 cm "
            "in heavy soils, 6-8 cm in light soils. Zero-tillage saves time and improves "
            "soil health. Raised bed planting saves 20-30% irrigation water and "
            "increases yield by 5-10%."
        ),
        "water_management": (
            "Critical irrigation stages: Crown Root Initiation (CRI, 20-25 DAS), tillering "
            "(40-45 DAS), late jointing (60-65 DAS), flowering (80-85 DAS), milking "
            "(95-100 DAS), and dough (110-115 DAS). Total water requirement: 400-500 mm "
            "in 4-6 irrigations. CRI stage irrigation is MOST critical—skipping reduces yield 25%."
        ),
        "fertilizer_recommendation": (
            "NPK at 120:60:40 kg/hectare for irrigated wheat. Apply full P, K and 1/3 N as "
            "basal. Top-dress remaining N at CRI (25 DAS) and tillering (45 DAS). Apply "
            "10-15 tonnes FYM/ha. Foliar spray of 2% urea at flowering boosts grain yield. "
            "Zinc sulfate (25 kg/ha) recommended in deficient soils."
        ),
        "common_pests": (
            "1) Aphids — suck sap, transmit viruses; spray Imidacloprid 17.8% SL @ 100 ml/"
            "ha. 2) Termites — damage roots; apply Chlorpyrifos 20 EC @ 4 L/ha to soil. "
            "3) Pink Stem Borer — causes deadheart; spray Coragen or Cypermethrin. "
            "4) Army Worm — defoliates leaves; spray Quinalphos 25 EC @ 1 L/ha."
        ),
        "common_diseases": (
            "1) Yellow Rust (Puccinia striiformis) — yellow stripes on leaves; spray "
            "Propiconazole 25 EC @ 0.1%. 2) Brown Rust — orange-brown pustules; same "
            "treatment. 3) Loose Smut — black powdery spikes; use treated seed only. "
            "4) Karnal Bunt — partial grain infection; resistant varieties + Tilt spray. "
            "5) Powdery Mildew — white powdery growth; spray Hexaconazole or sulfur."
        ),
        "harvesting": (
            "Harvest when grain moisture is 20-25% (hard dough stage) and straw turns "
            "golden yellow. Combine harvester is most efficient. Manual harvesting: cut "
            "with sickle, bundle, sun-dry 4-7 days, then thresh. Dry grain to 12% moisture "
            "for safe long-term storage."
        ),
        "average_yield": (
            "Traditional varieties: 1.5-2.5 t/ha. Modern HYVs: 4-5 t/ha. Best management: "
            "6-7 t/ha. Indian average: 3.5 t/ha. Punjab average: 5.2 t/ha (highest in India). "
            "World record: 17 t/ha (UK). Bangladesh: 3.2 t/ha average."
        ),
    },

    # ============================================================
    # 3. MAIZE (Zea mays)
    # ============================================================
    "maize": {
        "scientific_name": "Zea mays",
        "family": "Poaceae (Grass family)",
        "overview": (
            "Maize (corn) is the world's most produced cereal crop after rice and wheat, "
            "and the queen of cereals for its versatility. Used for food, feed, fodder, "
            "and biofuel. Grown across temperate, subtropical, and tropical zones. India "
            "produces ~30 million tonnes annually; major states are Karnataka, MP, Bihar."
        ),
        "soil_requirements": (
            "Maize thrives in well-drained, deep, fertile loam to sandy-loam soils with "
            "good organic matter. Optimal pH: 5.5 to 7.5. Avoid waterlogged or saline "
            "soils—maize is highly sensitive to waterlogging at all stages. Heavy clay "
            "soils need proper drainage. Soil should hold 50% available water."
        ),
        "climate_requirements": (
            "Warm-season crop. Optimal temperature: 21-27°C for vegetative growth, 18-22°C "
            "at night during grain filling. Germination needs 18°C+ soil temperature. "
            "Sensitive to frost at all stages. Requires 500-800 mm well-distributed "
            "rainfall. Long-day plant—12-14 hours of daylight ideal."
        ),
        "growing_season": (
            "Three seasons in India: Kharif (June-October, main season), Rabi (October-"
            "March, irrigated), and Spring (January-May). Tropical/subtropical zones grow "
            "year-round. Crop duration: 70-110 days for grain, 50-70 days for green cobs."
        ),
        "popular_varieties": (
            "Hybrid varieties (most productive): HQPM-1, HQPM-5 (Quality Protein Maize), "
            "DHM-117, Pioneer 3401, Bisco 855, NK-6240, Syngenta NK-30. Composites: "
            "Vivek QPM-9, Pusa Composite 3. Sweet corn: Sugar-75, Madhuri. Baby corn: "
            "VL Baby Corn-1, HM-4."
        ),
        "seed_preparation": (
            "Seed rate: 20-25 kg/ha for hybrids, 25-30 kg/ha for composites. Treat seeds "
            "with Thiram (2 g/kg) and Imidacloprid (5 ml/kg) against soil pests. Soak "
            "seeds in water for 6-8 hours before sowing to improve germination. Use only "
            "fresh, certified seed—maize seed viability drops fast."
        ),
        "sowing_method": (
            "Row spacing: 60-75 cm; plant-to-plant: 20-25 cm. Plant population: 65,000-"
            "75,000 plants/ha for grain; 80,000+ for fodder. Sowing depth: 4-5 cm. Ridge "
            "and furrow method preferred for kharif. Raised beds save 30% water and "
            "improve aeration."
        ),
        "water_management": (
            "Critical stages: knee-high (30-35 DAS), tasseling (45-50 DAS), silking (55-60 "
            "DAS), grain filling (70-80 DAS). Water stress at silking reduces yield by "
            "50%! Drip irrigation increases water-use efficiency by 40%. Total water "
            "need: 500-700 mm. Drain immediately after rains—maize hates waterlogging."
        ),
        "fertilizer_recommendation": (
            "NPK at 150:75:60 kg/ha for hybrid maize. Apply full P, K and 1/3 N at sowing. "
            "Top-dress N: 1/3 at knee-high stage (30 DAS), 1/3 at tasseling (50 DAS). "
            "Apply 10-15 tonnes FYM/ha. Zinc sulfate (25 kg/ha) is essential—maize is "
            "highly responsive to Zn. Foliar spray of 19:19:19 NPK at tasseling boosts grain."
        ),
        "common_pests": (
            "1) Fall Armyworm (Spodoptera frugiperda) — recent invasive pest, devastating; "
            "use Emamectin Benzoate 5% SG @ 100 g/ha or Spinetoram. 2) Stem Borer (Chilo "
            "partellus) — bores into stems causing deadheart; apply Carbofuran 3G in whorl. "
            "3) Shoot Fly — early-stage damage; treat seed with Imidacloprid. 4) Pink Stem "
            "Borer — late-season; same treatment as Chilo."
        ),
        "common_diseases": (
            "1) Turcicum Leaf Blight — large cigar-shaped lesions; spray Mancozeb @ 0.25%. "
            "2) Maydis Leaf Blight — small spots; same treatment. 3) Banded Leaf and "
            "Sheath Blight — banded lesions; spray Carbendazim. 4) Downy Mildew — "
            "yellow streaks, stunted plants; treat seed with Metalaxyl. 5) Charcoal Rot — "
            "stalk rot at maturity; resistant varieties + balanced N."
        ),
        "harvesting": (
            "Harvest when husks dry and turn brown, kernels are hard and shiny, and grain "
            "moisture is 20-25%. Black layer at kernel base indicates physiological "
            "maturity. Pick cobs by hand or combine harvester. Dry to 14% moisture for "
            "storage. Sweet corn: harvest at milk stage (20-24 days after silking) when "
            "kernels exude milky liquid."
        ),
        "average_yield": (
            "Composite varieties: 2-4 t/ha. Hybrids: 6-8 t/ha. Best management hybrids: "
            "10-12 t/ha. World record: 28 t/ha (USA). Indian average: 3.0 t/ha. "
            "Karnataka and Bihar averages exceed 4 t/ha."
        ),
    },

    # ============================================================
    # 4. POTATO (Solanum tuberosum)
    # ============================================================
    "potato": {
        "scientific_name": "Solanum tuberosum",
        "family": "Solanaceae (Nightshade family)",
        "overview": (
            "Potato is the world's fourth-largest food crop after rice, wheat, and maize. "
            "It is a cool-season tuber crop native to the Andes mountains of South America. "
            "Highly nutritious—rich in carbohydrates, vitamin C, potassium, and B-vitamins. "
            "India is the second-largest producer globally after China."
        ),
        "soil_requirements": (
            "Potato thrives in well-drained, loose, sandy-loam to loamy soils. Optimal pH "
            "is 5.0 to 6.5—slightly acidic soils reduce scab disease. Avoid heavy clay "
            "soils that cause tuber deformation. Deep soil (minimum 30 cm depth) is "
            "essential for tuber development. Organic matter should exceed 2%."
        ),
        "climate_requirements": (
            "Cool-season crop. Optimal temperature: 15-25°C during the day and 10-15°C "
            "at night. Tuber formation halts above 30°C. Frost damages foliage. Requires "
            "500-700 mm of well-distributed rainfall or equivalent irrigation."
        ),
        "growing_season": (
            "In North India: October-February (rabi). Hill regions: April-September. "
            "Bangladesh: November-February. Crop duration is 90-120 days depending on "
            "variety. Plant when soil temperature reaches 15-20°C."
        ),
        "popular_varieties": (
            "Kufri Jyoti (versatile), Kufri Bahar (early, high-yielding), Kufri Pukhraj "
            "(early, processing), Kufri Chipsona-1/3 (chips processing), Kufri Sindhuri "
            "(red-skinned), Kufri Lalima, Kufri Khyati (drought-tolerant). For processing: "
            "Atlantic, Lady Rosetta. Bangladesh: Diamant, Cardinal, Granola."
        ),
        "seed_preparation": (
            "Use certified disease-free seed tubers of 30-50 g size. Whole tubers preferred; "
            "if cutting, each piece must have 2-3 eyes. Treat seed with Mancozeb (0.25%) "
            "for 10 minutes. Sprout tubers in diffused light for 2-3 weeks before planting."
        ),
        "planting_method": (
            "Spacing: 60 cm between rows, 20 cm between plants. Planting depth: 5-7 cm. "
            "Seed rate: 25-30 quintals/hectare. Earthing-up done twice—first at 30 DAS "
            "and second at 45-50 DAS—to prevent tuber greening and promote tuber bulking."
        ),
        "water_management": (
            "Critical irrigation stages: stolon formation (30-35 DAS), tuber initiation "
            "(45-50 DAS), tuber bulking (60-75 DAS). Maintain field capacity moisture. "
            "Avoid waterlogging—causes tuber rot. Stop irrigation 10-15 days before harvest."
        ),
        "fertilizer_recommendation": (
            "NPK at 180:80:100 kg/ha is standard. Apply full P and K plus half N as basal. "
            "Top-dress remaining N at earthing-up (30-40 DAS). Add 25-30 tonnes FYM/ha. "
            "Foliar spray of 19:19:19 NPK at 0.5% during tuber bulking boosts yield."
        ),
        "common_pests": (
            "1) Potato Tuber Moth — larvae bore into tubers; use pheromone traps and "
            "Spinosad. 2) Aphids — vectors for viral diseases; spray Imidacloprid. "
            "3) Cutworms — cut seedlings at ground level; apply Chlorpyrifos to soil. "
            "4) White Grubs — feed on tubers; treat soil with Phorate granules."
        ),
        "common_diseases": (
            "1) Late Blight (Phytophthora infestans) — caused Irish famine; dark water-"
            "soaked lesions; spray Metalaxyl + Mancozeb preventively. 2) Early Blight — "
            "concentric rings on leaves; use Mancozeb. 3) Black Scurf — black sclerotia "
            "on tubers; treat seed with Tolclofos-methyl. 4) Bacterial Wilt — sudden "
            "wilting; resistant varieties + crop rotation. 5) Common Scab — corky lesions; "
            "maintain soil pH below 5.5."
        ),
        "harvesting": (
            "Harvest when foliage turns yellow and starts drying (90-120 DAS). Dehaulm "
            "(cut tops) 10-15 days before digging to harden skin. Dig carefully to avoid "
            "bruising. Cure tubers in shade for 10-15 days before storage."
        ),
        "average_yield": (
            "Average: 20-25 tonnes/hectare. Improved varieties under good management: "
            "30-40 tonnes/ha. Top farmers achieve 50+ tonnes/ha. Indian average: 22 t/ha; "
            "Netherlands averages 45 t/ha (world leader)."
        ),
        "storage": (
            "Store at 2-4°C for table potatoes and 8-10°C for processing. Maintain 90-95% "
            "relative humidity. Cold storage extends shelf life to 6-8 months. Avoid light "
            "exposure—causes greening and solanine formation."
        ),
    },

    # ============================================================
    # 5. TOMATO (Solanum lycopersicum)
    # ============================================================
    "tomato": {
        "scientific_name": "Solanum lycopersicum",
        "family": "Solanaceae (Nightshade family)",
        "overview": (
            "Tomato is the world's most popular vegetable crop and a major source of "
            "lycopene, vitamin C, and potassium. It is a warm-season annual grown for "
            "fresh consumption and processing (paste, sauce, juice). India is the "
            "second-largest producer globally."
        ),
        "soil_requirements": (
            "Tomato grows best in well-drained sandy-loam to clay-loam soils rich in "
            "organic matter. Optimal pH: 6.0 to 7.0. Avoid waterlogged or saline soils. "
            "Soil temperature should be above 16°C for transplanting. Crop rotation "
            "essential—do not grow after potato, brinjal, or chili."
        ),
        "climate_requirements": (
            "Warm-season crop. Optimal temperature: 20-27°C during day, 15-20°C at night. "
            "Fruit set fails above 35°C or below 10°C. Sensitive to frost. Requires "
            "moderate rainfall (600-1250 mm) but excess humidity promotes fungal diseases. "
            "Needs 6-8 hours of direct sunlight daily."
        ),
        "growing_season": (
            "Three seasons in India: Kharif (June-July), Rabi (October-November), Summer "
            "(January-February). Hill regions: March-April. Polyhouse cultivation allows "
            "year-round production. Crop duration: 110-150 days."
        ),
        "popular_varieties": (
            "Determinate: Pusa Ruby, Pusa Early Dwarf, Arka Vikas, Arka Saurabh. "
            "Indeterminate: Arka Rakshak (triple disease resistant), Arka Samrat, Pusa "
            "Hybrid 2/4. Hybrid F1: Heem Sohna, Naveen 2000, Avtar. Cherry: Punjab Red "
            "Cherry, Solan Red Round."
        ),
        "nursery_management": (
            "Sow seeds in raised nursery beds or pro-trays with cocopeat. Seed rate: "
            "400-500 g/hectare. Treat seeds with Thiram (3 g/kg) and Trichoderma viride "
            "(10 g/kg). Seedlings ready for transplanting in 25-30 days at 4-6 true leaf "
            "stage. Harden 5 days before transplanting."
        ),
        "transplanting": (
            "Spacing: 60x45 cm for determinate, 75x60 cm for indeterminate. Transplant in "
            "evening hours. Water immediately after transplanting. Staking required for "
            "indeterminate varieties—improves yield by 30-40%."
        ),
        "water_management": (
            "Critical stages: flowering, fruit set, fruit development. Irrigate every 4-5 "
            "days in summer, 7-10 days in winter. Drip irrigation saves 40% water and "
            "prevents foliar diseases. Water requirement: 600-800 mm. Mulching with black "
            "plastic conserves moisture."
        ),
        "fertilizer_recommendation": (
            "NPK at 120:80:60 kg/ha. Apply 25-30 tonnes FYM/ha. Full P and K + 1/3 N "
            "basal; remaining N in two splits at 30 and 60 DAT. Calcium deficiency causes "
            "blossom end rot—spray Calcium Nitrate (1%) at flowering. Boron at 0.2% "
            "improves fruit set."
        ),
        "training_and_pruning": (
            "Remove side shoots (suckers) regularly to maintain 1-2 main stems. Top the "
            "plant after 5-7 trusses. Remove yellow lower leaves to improve air "
            "circulation. Pruning increases fruit size and reduces disease incidence."
        ),
        "common_pests": (
            "1) Fruit Borer (Helicoverpa armigera) — bores into fruits; use Bt sprays, "
            "pheromone traps (5/acre), Emamectin Benzoate. 2) Whitefly — vector for Tomato "
            "Leaf Curl Virus; yellow sticky traps + Diafenthiuron. 3) Tomato Pinworm "
            "(Tuta absoluta) — devastating new pest; Cyantraniliprole. 4) Red Spider "
            "Mite — yellow stippling; Propargite or sulfur."
        ),
        "common_diseases": (
            "1) Early Blight (Alternaria solani) — concentric rings; Mancozeb or "
            "Chlorothalonil. 2) Late Blight — water-soaked lesions; Metalaxyl + Mancozeb. "
            "3) Tomato Leaf Curl Virus (ToLCV) — control whitefly. 4) Bacterial Wilt — "
            "grafted plants on resistant rootstock. 5) Fusarium Wilt — use Arka Rakshak."
        ),
        "physiological_disorders": (
            "1) Blossom End Rot — calcium deficiency; foliar Ca spray. 2) Fruit Cracking — "
            "irregular moisture; mulch + consistent irrigation. 3) Sunscald — maintain "
            "foliage cover. 4) Catfacing — cold stress during flowering."
        ),
        "harvesting": (
            "Harvest at appropriate maturity: Mature green (distant markets), Pink/Turning "
            "(local), Red ripe (processing). Pick every 3-4 days. Harvest in cool morning "
            "hours. Average 8-12 pickings per crop."
        ),
        "average_yield": (
            "Open-field traditional: 25-35 t/ha. Open-field hybrids: 50-80 t/ha. "
            "Polyhouse: 100-150 t/ha. World average: 38 t/ha; Netherlands polyhouse: "
            "500+ t/ha (world record)."
        ),
    },

    # ============================================================
    # 6. ONION (Allium cepa)
    # ============================================================
    "onion": {
        "scientific_name": "Allium cepa",
        "family": "Amaryllidaceae (Onion family)",
        "overview": (
            "Onion is one of the most important commercial vegetable crops worldwide and "
            "a staple flavoring ingredient in nearly every cuisine. India is the world's "
            "second-largest producer after China. Maharashtra (especially Nashik), "
            "Karnataka, Gujarat, and Madhya Pradesh are key onion-growing states. "
            "Both bulb and leaf onions are cultivated."
        ),
        "soil_requirements": (
            "Onion grows best in well-drained sandy-loam to silt-loam soils rich in "
            "organic matter. Optimal pH: 6.0-7.5. Avoid heavy clay (causes deformed bulbs) "
            "and sandy soils (low water retention). Saline-alkaline soils reduce yield "
            "drastically. Soil should be deeply tilled to 25-30 cm."
        ),
        "climate_requirements": (
            "Cool-season biennial grown as annual. Optimal temperature: 13-25°C for "
            "vegetative growth, 15-25°C for bulb formation. Long days (>13 hours) favor "
            "bulbing in temperate varieties; short days for tropical varieties. Sensitive "
            "to frost during bulb formation. Requires 650-750 mm well-distributed water."
        ),
        "growing_season": (
            "Three main seasons in India: Kharif (June-October), Late Kharif (August-"
            "January), Rabi (October-April). Rabi is the main season producing 60% of "
            "India's onions. Bangladesh: November-March main crop. Crop duration: 140-160 "
            "days from seed; 100-110 days from sets."
        ),
        "popular_varieties": (
            "Red varieties: Nashik Red (Maharashtra famous), Bhima Super, Bhima Red, "
            "Agrifound Dark Red, Pusa Red. White: Pusa White Round, Bhima Shubhra. "
            "Yellow: Arka Pitamber. Hybrid: Bhima Kiran (red), Phule Suvarna (yellow). "
            "Long-storage: Bhima Kiran, N-2-4-1."
        ),
        "nursery_management": (
            "Seed rate: 8-10 kg/hectare. Sow in raised nursery beds (1m wide, convenient "
            "length, 15 cm high). Treat seeds with Thiram or Captan (2 g/kg). Seedlings "
            "ready for transplanting in 6-8 weeks at pencil thickness. Apply 10-15 tonnes "
            "FYM in nursery beds."
        ),
        "transplanting": (
            "Spacing: 15 cm row-to-row, 10 cm plant-to-plant. Plant population: 6-7 lakh "
            "plants/hectare. Plant on flat beds or ridges. Transplant in evening hours. "
            "Water immediately after transplanting. Apply mulch to conserve moisture and "
            "reduce weeds."
        ),
        "water_management": (
            "Critical stages: establishment (first 2 weeks), bulb formation (60-90 DAT), "
            "bulb development (90-120 DAT). Light frequent irrigations preferred—every "
            "7-10 days in winter, 5-7 days in summer. Stop irrigation 10-15 days before "
            "harvest for proper bulb curing. Drip irrigation saves 30-40% water."
        ),
        "fertilizer_recommendation": (
            "NPK at 100:50:50 kg/hectare. Apply full P and K plus half N as basal. "
            "Top-dress remaining N in two splits at 30 and 45 DAT. Apply 20-25 tonnes "
            "FYM/ha. Sulfur (30-40 kg/ha) is essential for pungency and bulb size. Avoid "
            "excess N—causes thick neck and poor storage."
        ),
        "common_pests": (
            "1) Thrips — most serious pest; silvery streaks on leaves; spray Spinosad or "
            "Fipronil 5% SC. 2) Onion Maggot — larvae bore into bulbs; soil drench with "
            "Chlorpyrifos. 3) Cutworms — cut seedlings at base; baiting with Carbaryl. "
            "4) Eriophyid Mites — twisted leaves; spray Dicofol."
        ),
        "common_diseases": (
            "1) Purple Blotch (Alternaria porri) — purple spots with concentric rings; "
            "spray Mancozeb or Hexaconazole. 2) Stemphylium Blight — yellow-brown spots; "
            "same treatment. 3) Downy Mildew — pale yellow patches in cool wet weather; "
            "spray Metalaxyl + Mancozeb. 4) Basal Rot — bulbs rot from base; treat seed "
            "with Trichoderma. 5) Onion Smut — black sooty masses; resistant varieties."
        ),
        "harvesting": (
            "Harvest when 50-70% of tops fall over (neck breakage) and outer scales turn "
            "papery. Bulbs achieve full size and color. Dig carefully with hand fork. Cure "
            "in field for 3-5 days under partial shade. Top removal and grading after curing."
        ),
        "average_yield": (
            "Traditional varieties: 15-20 t/ha. Improved varieties: 25-35 t/ha. Best "
            "management hybrids: 40-50 t/ha. World record: 80+ t/ha. Indian average: "
            "17 t/ha; Maharashtra average: 18-20 t/ha."
        ),
        "storage": (
            "Cure bulbs properly (10-14 days) until necks are dry. Store at 0-2°C with "
            "65-70% humidity for long-term (6+ months). Traditional storage: well-"
            "ventilated structures with raised platforms. Avoid moisture and direct sun. "
            "Storage losses can reach 30-50% in poor storage."
        ),
    },

    # ============================================================
    # 7. MANGO (Mangifera indica)
    # ============================================================
    "mango": {
        "scientific_name": "Mangifera indica",
        "family": "Anacardiaceae (Cashew family)",
        "overview": (
            "Mango is called the 'King of Fruits' and the national fruit of India, "
            "Pakistan, and the Philippines. It is the most economically important "
            "tropical fruit globally. India produces ~21 million tonnes (40% of world "
            "production), with Uttar Pradesh, Andhra Pradesh, Karnataka, and Bihar as "
            "top producers. Trees can live 100+ years and bear for 60+ years."
        ),
        "soil_requirements": (
            "Mango grows well in deep, well-drained alluvial or red loam soils. Optimal "
            "pH: 5.5-7.5. Soil depth should be at least 2-3 meters for proper root "
            "development. Tolerates moderate salinity. Avoid waterlogged soils—mango is "
            "extremely sensitive to root suffocation. Light sandy soils with good organic "
            "matter also suitable."
        ),
        "climate_requirements": (
            "Tropical to subtropical. Optimal temperature: 24-30°C. Survives 4-46°C "
            "extremes when mature. Distinct dry period (2-3 months) before flowering is "
            "essential for good flowering. Frost kills young plants and damages flowers. "
            "Annual rainfall of 750-2500 mm ideal but dry weather during flowering "
            "essential."
        ),
        "growing_season": (
            "Planting: monsoon (June-August) in dry regions; February-March in wet regions. "
            "Flowering: December-February in North India; October-December in South. "
            "Fruiting: April-July (North), March-June (South). Trees start bearing in "
            "4-5 years (grafted) or 7-10 years (seedling). Peak production: 15-30 years."
        ),
        "popular_varieties": (
            "North India: Dasheri, Langra, Chausa, Mallika, Amrapali, Bombay Green. "
            "South India: Alphonso (king of varieties), Kesar, Banganapalli, Neelum, "
            "Totapuri, Raspuri. East India: Himsagar, Langra, Fazli, Gulab Khas. "
            "Bangladesh: Himsagar, Langra, Fazli, Amrapali, Gopalbhog. Export: Alphonso, "
            "Kesar, Banganapalli."
        ),
        "propagation": (
            "Grafting is the standard method—Veneer Grafting (best), Side Grafting, or "
            "Approach Grafting. Use 1-year-old rootstocks (Olour, Kalapady recommended). "
            "Avoid seedling propagation—takes longer to bear and varieties don't come "
            "true. Air-layering also possible for some varieties. Grafted plants ready "
            "for field planting at 9-12 months."
        ),
        "planting": (
            "Spacing: 10x10 meters for standard varieties (100 plants/ha); 5x5 meters "
            "for dwarf/Amrapali (400 plants/ha); high-density: 2.5x2.5 m (1600 plants/ha). "
            "Pit size: 1x1x1 meter, filled with FYM, soil, and rock phosphate. Plant at "
            "the start of monsoon or in February. Stake young plants and provide shade "
            "for first 2 years."
        ),
        "water_management": (
            "Young plants: irrigate every 2-3 days in summer, weekly in winter, for first "
            "3 years. Mature trees: critical irrigation during fruit set and development "
            "(March-May). Avoid irrigation 2-3 months before flowering—dry stress promotes "
            "flowering. Drip irrigation saves 50% water and increases yield by 20-30%."
        ),
        "fertilizer_recommendation": (
            "Per mature tree (10+ years): 1 kg N + 0.5 kg P + 1 kg K + 50 kg FYM annually, "
            "split into two doses (June and October). Young trees: 100 g N + 50 g P + 100 g "
            "K per year of age. Foliar spray of 2% urea before flowering boosts fruit set. "
            "Apply micronutrients (Zn, B, Fe) every 2-3 years."
        ),
        "training_and_pruning": (
            "Train young plants to develop strong scaffold branches at 60-100 cm height. "
            "Annual pruning of mature trees: remove dead, diseased, crossing, and water-"
            "sprout branches after harvest (July-August). Open canopy improves light "
            "penetration and reduces disease. Rejuvenation pruning every 10-15 years for "
            "old trees."
        ),
        "common_pests": (
            "1) Mango Hopper — most serious pest; sucks sap from flowers, causes flower "
            "drop; spray Imidacloprid 17.8% SL @ 0.5 ml/L at flower bud stage. 2) Mealy "
            "Bug — apply slippery bands on trunk + spray Chlorpyrifos. 3) Fruit Fly — "
            "use pheromone traps (Methyl Eugenol) + bagging fruits. 4) Stem Borer — "
            "swab Chlorpyrifos paste on holes. 5) Scale Insects — spray dimethoate."
        ),
        "common_diseases": (
            "1) Powdery Mildew (Oidium mangiferae) — white powder on flowers/young fruits, "
            "causes massive flower drop; spray Sulfur 0.2% or Hexaconazole at flower bud "
            "stage. 2) Anthracnose (Colletotrichum) — black spots on leaves/fruits; spray "
            "Carbendazim or Mancozeb. 3) Mango Malformation — distorted shoots/panicles; "
            "remove and burn affected parts. 4) Bacterial Canker — copper sprays. "
            "5) Die-back — prune affected branches + Bordeaux paste."
        ),
        "harvesting": (
            "Harvest when fruits develop characteristic color, shoulders fill out, and "
            "specific gravity (1.01-1.02) is right. Use mango plucker (pole with cutting "
            "device and bag) to avoid bruising. Leave 5 cm stalk attached. Harvest in "
            "cool morning hours. Pre-harvest dipping in Carbendazim (0.1%) extends shelf "
            "life. Hot water treatment (52°C for 5 min) controls anthracnose."
        ),
        "average_yield": (
            "Traditional planting: 40-80 fruits/tree (8-15 kg). Mature productive tree: "
            "200-500 fruits (50-100 kg). High-density orchards: 15-20 t/ha. Best management: "
            "25-30 t/ha. World average: 8 t/ha. India: 7.5 t/ha. Productivity per tree "
            "increases 30-50% with proper canopy management."
        ),
        "post_harvest": (
            "Ripen at 25-30°C with proper ventilation for 8-10 days. Commercial ripening "
            "uses Ethylene gas (100 ppm) for 24 hours. Storage at 12-13°C for 3-4 weeks. "
            "Below 10°C causes chilling injury. Sort and grade by size, color, and quality. "
            "Pack in ventilated cartons with paper cushioning."
        ),
    },

    # ============================================================
    # 8. BANANA (Musa spp.)
    # ============================================================
    "banana": {
        "scientific_name": "Musa acuminata, Musa balbisiana",
        "family": "Musaceae (Banana family)",
        "overview": (
            "Banana is the world's most consumed fruit and the fourth most important food "
            "crop globally after rice, wheat, and maize. It is grown in 130+ countries. "
            "India is the world's largest producer (~30 million tonnes, 26% of world). "
            "Major Indian states: Tamil Nadu, Maharashtra, Gujarat, Andhra Pradesh. "
            "A perennial herb, NOT a tree—the 'trunk' is a pseudostem of leaf sheaths."
        ),
        "soil_requirements": (
            "Banana thrives in deep, well-drained, fertile alluvial loam or clay-loam "
            "soils. Optimal pH: 6.0-7.5. Soil depth: minimum 1.5 meters. Heavy clay and "
            "waterlogged soils unsuitable. Tolerates light salinity. High organic matter "
            "(>2%) essential. Tissue culture plants need extra-careful soil preparation."
        ),
        "climate_requirements": (
            "Tropical humid crop. Optimal temperature: 27-30°C (range 15-38°C). Frost "
            "kills banana. Strong winds cause major losses—choose sheltered locations or "
            "use wind-breaks. Annual rainfall: 1500-2500 mm well-distributed. Requires "
            "high humidity (75-85%). Sensitive to drought during fruit development."
        ),
        "growing_season": (
            "Planting can be done year-round in tropical climates, but optimal timing: "
            "February-April or August-November. Crop duration: 11-15 months from planting "
            "to harvest. Ratoon crops (2-3 cycles) extend production from same field. "
            "Bangladesh: March-April optimal planting; harvest in 12-14 months."
        ),
        "popular_varieties": (
            "Cavendish group (export quality): Grand Naine (most popular), Robusta, "
            "Williams. AAB Plantain: Nendran (Kerala). Other Indian varieties: Dwarf "
            "Cavendish, Poovan, Rasthali, Red Banana, Karpuravalli, Nyali. Bangladesh: "
            "Sagor (Cavendish), Champa, Mehersagar, Sabri. Disease-resistant: Tissue "
            "culture Grand Naine."
        ),
        "planting_material": (
            "Best: Tissue culture plants (disease-free, uniform, 15-20% higher yield). "
            "Traditional: Sword suckers (1.5-2 kg, with sword-shaped leaves) or bits "
            "(corms cut into 1 kg pieces). Treat suckers with Carbendazim (0.1%) + "
            "Chlorpyrifos (0.05%) for 30 minutes before planting. Tissue culture plants "
            "should be hardened 1 month in nursery before field planting."
        ),
        "planting": (
            "Spacing: 1.8x1.8 m (Cavendish, 3,086 plants/ha), 2x2 m (tall varieties, "
            "2,500 plants/ha), or high-density 1.5x1.5 m (4,400 plants/ha). Pit size: "
            "0.6x0.6x0.6 m, filled with topsoil + 10 kg FYM + 250 g neem cake + 100 g "
            "Trichoderma. Plant at soil level—deep planting causes corm rot. Mulch with "
            "dry leaves immediately."
        ),
        "water_management": (
            "Heavy water demander: 2000-2500 mm per cycle. Drip irrigation strongly "
            "recommended—saves 40-50% water, increases yield by 25-30%. Irrigate every "
            "3-4 days in summer, weekly in winter. Critical stages: 3-5 months (vegetative), "
            "6-8 months (flowering), 8-11 months (fruit development). Mulching essential."
        ),
        "fertilizer_recommendation": (
            "Heavy feeder: 200:60:300 g NPK per plant per cycle. Apply in 6-8 splits "
            "starting from 3 months. Apply 10 kg FYM + 100 g neem cake per plant before "
            "planting. Top-dressing schedule (per plant): 25g N, 7g P, 50g K at 30, 60, "
            "90, 120, 150, 180, 240, 300 DAP. Foliar K spray at flowering improves "
            "fruit quality."
        ),
        "intercultural_operations": (
            "Earthing-up: at 4 and 6 months to support pseudostem. Desuckering: remove "
            "all suckers except one healthy follower for ratoon. Propping: bamboo support "
            "after flowering to prevent toppling under fruit weight. Denavelling: remove "
            "male bud after last hand of fruits sets—improves fruit size by 10%. "
            "Bunch covering: blue polythene sleeves protect from pests and improve quality."
        ),
        "common_pests": (
            "1) Banana Rhizome Weevil (Cosmopolites sordidus) — larvae bore into corm; "
            "use pheromone traps + Chlorpyrifos drench. 2) Pseudostem Weevil — inject "
            "Monocrotophos into pseudostem. 3) Nematodes (Pratylenchus, Radopholus) — "
            "rotate with paddy + apply Carbofuran 3G. 4) Thrips — silvering on fruits; "
            "spray Fipronil. 5) Aphids — vectors for Bunchy Top Virus; control immediately "
            "with Imidacloprid."
        ),
        "common_diseases": (
            "1) Panama Wilt (Fusarium oxysporum f.sp. cubense Race 4) — devastating soil-"
            "borne disease, no cure; use resistant tissue culture varieties + soil "
            "drenching with Carbendazim. 2) Sigatoka Leaf Spot (Black/Yellow) — yellow "
            "streaks turning brown/black; spray Propiconazole or Mancozeb monthly. "
            "3) Bunchy Top Virus — bunched leaves, no fruit; rogue affected plants + "
            "control aphid vector. 4) Banana Streak Virus — yellow streaks; use clean "
            "planting material. 5) Anthracnose — black spots on fruits; pre/post-harvest "
            "fungicide sprays."
        ),
        "harvesting": (
            "Harvest at 11-13 months when fingers are 3/4 mature, ridges become less "
            "prominent, and color changes from dark green to light green. Cut bunch with "
            "sharp knife, leaving 30 cm of stalk above first hand. Handle gently to avoid "
            "bruising. Dehand within 24 hours for transport. Field-pack in moist conditions "
            "to avoid latex stains."
        ),
        "average_yield": (
            "Traditional varieties: 25-30 t/ha. Improved varieties (Grand Naine) with good "
            "management: 60-80 t/ha. Tissue culture + drip irrigation + good management: "
            "80-100 t/ha. World record: 120 t/ha (India, Maharashtra). World average: "
            "20 t/ha. India: 35 t/ha; Maharashtra: 65 t/ha average."
        ),
        "post_harvest": (
            "Wash bunches, dehand, sort by size. Ripening: Ethylene gas (1000 ppm for "
            "24 hrs) at 18-20°C, 90% humidity. Natural ripening with calcium carbide is "
            "banned in many countries—use Ethylene. Storage at 13-14°C extends shelf life "
            "by 2-3 weeks. Below 12°C causes chilling injury (skin blackening). Pack in "
            "ventilated cartons of 13-14 kg for export."
        ),
    },

    # ============================================================
    # 9. COTTON (Gossypium hirsutum)
    # ============================================================
    "cotton": {
        "scientific_name": "Gossypium hirsutum (upland cotton, 90% world production)",
        "family": "Malvaceae (Mallow family)",
        "overview": (
            "Cotton is the world's most important fiber crop and the 'white gold' of "
            "agriculture. India is the world's largest cotton producer and consumer, "
            "growing on 12+ million hectares. Major states: Gujarat, Maharashtra, Telangana, "
            "Karnataka, Punjab, Haryana. Bt cotton (genetically modified for bollworm "
            "resistance) is grown on 95%+ of Indian cotton area."
        ),
        "soil_requirements": (
            "Cotton grows on a wide range of soils but prefers deep, well-drained black "
            "cotton soils (Vertisols) with high water retention. Optimal pH: 6.0-8.0. "
            "Tolerates moderate salinity (4-6 dS/m) better than most crops. Heavy clay "
            "and sandy soils both work with proper management. Soil depth: minimum 60 cm."
        ),
        "climate_requirements": (
            "Warm-season, frost-sensitive crop. Optimal temperature: 21-30°C. Requires "
            "6-7 frost-free months. Sensitive to temperatures above 38°C during flowering "
            "and below 16°C at any stage. Annual rainfall: 500-800 mm well-distributed. "
            "High humidity at flowering causes boll rot. Long sunny periods favor fiber "
            "development."
        ),
        "growing_season": (
            "Kharif crop in India: sowing May-July (rainfed) or April-May (irrigated). "
            "Harvest October-February. Crop duration: 160-200 days. North India: short-"
            "duration varieties for cotton-wheat rotation. Central/South India: long-"
            "duration varieties. Two-three pickings spread over 2-3 months."
        ),
        "popular_varieties": (
            "Bt Cotton Hybrids (dominant): RCH-2, RCH-659, Jadoo, Mallika, Bunny, Tulasi. "
            "Recent: NCS-2331, Rasi-660. Conventional hybrids: NHH-44, LRA-5166. Long-"
            "staple varieties for premium fiber: Suvin, Bunny Bt. Indigenous (Desi) "
            "cotton: G.arboreum varieties for niche markets. Organic cotton: non-Bt "
            "conventional varieties."
        ),
        "seed_preparation": (
            "Seed rate: 2.5 kg/ha for Bt hybrids (lower due to single seed per hill), "
            "10-15 kg/ha for non-Bt and Desi varieties. Use only delinted, treated seed. "
            "Seed treatment: Imidacloprid 70% WS @ 5-7 g/kg against sucking pests + "
            "Carbendazim @ 2 g/kg against seed-borne diseases. Pelleted Bt seed comes "
            "pre-treated."
        ),
        "sowing_method": (
            "Spacing for Bt hybrids: 90x60 cm or 120x60 cm (high-density planting 67-"
            "111 thousand plants/ha). Dibble 2 seeds per hill, thin to one at 15 DAS. "
            "Sowing depth: 3-5 cm. Sow on ridges in rainfed; on flat beds in irrigated. "
            "Refuge crop (non-Bt cotton or other crop) mandatory at 5 rows around Bt "
            "cotton field to delay resistance."
        ),
        "water_management": (
            "Total water requirement: 700-1300 mm. Critical stages: squaring (45-60 DAS), "
            "flowering (60-100 DAS), boll development (100-140 DAS). Water stress at "
            "flowering causes major yield loss. Drip irrigation increases yield by 25-30% "
            "and saves 40% water. Stop irrigation 20-30 days before final picking to "
            "ensure boll opening."
        ),
        "fertilizer_recommendation": (
            "NPK at 150:75:75 kg/ha for Bt hybrids; 80:40:40 kg/ha for desi cotton. Apply "
            "full P, K and 1/3 N as basal. Top-dress remaining N in two splits: at squaring "
            "(40-45 DAS) and flowering (60-70 DAS). Apply 10-15 tonnes FYM/ha. Foliar "
            "spray of 2% DAP + 1% MAP at flowering boosts boll formation. Magnesium and "
            "boron sprays improve fiber quality."
        ),
        "common_pests": (
            "1) Pink Bollworm (Pectinophora gossypiella) — major Bt-resistant pest; "
            "use pheromone traps (5/ha), Spinetoram, or Diamides; clear stubble after "
            "harvest. 2) Sucking pests (Whitefly, Jassids, Aphids, Thrips) — major in "
            "Bt cotton; spray Diafenthiuron, Imidacloprid, or Acetamiprid. 3) Mealy "
            "Bug — sticky honeydew; apply systemic insecticides + biological control "
            "with Cryptolaemus beetles. 4) American Bollworm — controlled by Bt cotton; "
            "monitor with pheromone traps. 5) Spotted Bollworm — pheromone traps + "
            "Chlorpyrifos."
        ),
        "common_diseases": (
            "1) Cotton Leaf Curl Virus (CLCuV) — yellowing, curling, vein thickening; "
            "control whitefly vector with Diafenthiuron; use resistant varieties. "
            "2) Bacterial Blight (Angular Leaf Spot) — angular water-soaked lesions; "
            "spray copper oxychloride + streptocycline. 3) Fusarium Wilt — wilting, "
            "vascular discoloration; use resistant varieties + Trichoderma soil "
            "application. 4) Verticillium Wilt — yellow mottling; same prevention. "
            "5) Boll Rot — fungal/bacterial complex in boll; improve ventilation, "
            "spray Mancozeb."
        ),
        "harvesting": (
            "Cotton bolls open over 60-90 days; multiple pickings needed (3-5 pickings "
            "at 15-20 day intervals). Hand-picking gives best quality—pick fully opened "
            "bolls in dry weather. Mechanical picking used in mechanized regions. Avoid "
            "picking wet cotton—causes spotting and quality loss. Sort by grade and "
            "store in dry, clean cotton bags."
        ),
        "average_yield": (
            "Rainfed traditional: 200-400 kg lint/ha. Irrigated Bt hybrid: 500-800 kg "
            "lint/ha (1500-2400 kg seed cotton). Best management: 1000-1500 kg lint/ha "
            "(3000-4500 kg seed cotton). High-density planting: 1500-2000 kg lint/ha. "
            "World average: 750 kg/ha; India: 460 kg/ha (one of lowest in major producers); "
            "Australia: 1900 kg/ha (world leader)."
        ),
        "post_harvest": (
            "Sun-dry cotton for 1-2 days to reduce moisture below 8%. Ginning separates "
            "fiber (lint) from seeds—ginning percentage typically 33-38%. Store cleaned "
            "lint in moisture-free conditions. Cottonseed is valuable byproduct: extract "
            "oil (16-20% by weight) and use cake as cattle feed. Grade cotton by staple "
            "length, strength, fineness, and trash content."
        ),
    },

    # ============================================================
    # 10. LENTIL (Lens culinaris)
    # ============================================================
    "lentil": {
        "scientific_name": "Lens culinaris",
        "family": "Fabaceae (Legume family)",
        "overview": (
            "Lentil (Masoor) is one of the oldest cultivated crops and an important "
            "pulse providing protein (25%), iron, and folate. It is a cool-season legume "
            "that fixes atmospheric nitrogen, improving soil fertility. India is the "
            "world's largest producer (~1.2 million tonnes) and consumer. Major states: "
            "Madhya Pradesh, Uttar Pradesh, Bihar, West Bengal. Bangladesh is also a "
            "significant producer."
        ),
        "soil_requirements": (
            "Lentil prefers well-drained loam to clay-loam soils with good moisture "
            "retention. Optimal pH: 6.0-7.5. Tolerates light salinity. Avoid waterlogged "
            "soils—lentil is highly sensitive to water stagnation. Soils with good organic "
            "matter and previous rice crop (rice fallow) work excellent. Soil depth: "
            "minimum 30 cm."
        ),
        "climate_requirements": (
            "Cool-season crop. Optimal temperature: 18-30°C during growth, 24-27°C at "
            "flowering. Sensitive to frost during flowering and pod formation. Drought-"
            "tolerant once established. Annual rainfall: 300-450 mm sufficient. High "
            "humidity and heavy rains cause foliar diseases and reduce yield significantly."
        ),
        "growing_season": (
            "Rabi crop: sowing October-November, harvest February-April. Crop duration: "
            "100-130 days. Rice-fallow cultivation popular in Eastern India—lentil sown "
            "after rice harvest using residual moisture. Bangladesh: November-February. "
            "Late sowing (after December) reduces yield by 20-30% due to terminal heat."
        ),
        "popular_varieties": (
            "Bold-seeded (preferred for dal): Pusa Vaibhav, IPL-220, IPL-316, JL-3, "
            "WBL-77 (West Bengal). Small-seeded: Pusa-4, Pusa-6, K-75, L-4076. Rust-"
            "resistant: HUL-57, IPL-81 (Noori). Wilt-resistant: VL Masoor-126, IPL-406. "
            "Bangladesh: BARI Masoor 4, 5, 6, 7 (rust resistant)."
        ),
        "seed_preparation": (
            "Seed rate: 30-40 kg/ha for bold-seeded varieties; 25-30 kg/ha for small-"
            "seeded. Treat seeds with Trichoderma viride (5-10 g/kg) + Rhizobium "
            "leguminosarum culture (10 g/kg) for nitrogen fixation. Fungicide treatment "
            "with Carbendazim (2 g/kg) + Thiram (1 g/kg) against seed-borne fungi. "
            "Soak in water 4-6 hours before sowing in rice-fallow conditions."
        ),
        "sowing_method": (
            "Line sowing recommended: row spacing 25-30 cm, depth 4-6 cm. Plant population: "
            "33-40 lakh plants/hectare. Broadcasting acceptable in rice fallows. Sow on "
            "raised beds in heavy soils or waterlogging-prone areas. Zero tillage works "
            "well after rice harvest—saves time, water, and improves soil structure."
        ),
        "water_management": (
            "Lentil is mostly grown rainfed on residual moisture. If irrigation available: "
            "first at pre-flowering (45-50 DAS), second at pod-filling (70-75 DAS). Over-"
            "irrigation causes vegetative growth at expense of pods and increases diseases. "
            "Drainage critical in heavy rains—lentil roots die in 24 hours of waterlogging."
        ),
        "fertilizer_recommendation": (
            "NPK at 20:40:20 kg/ha as basal application—lentil needs little N due to "
            "biological nitrogen fixation. Apply 5-10 tonnes FYM/ha. Sulfur (20-30 kg/ha) "
            "boosts protein content and yield. Foliar spray of 2% urea at flowering "
            "improves pod-setting. Zinc and boron deficient soils need micronutrient "
            "application (Zn @ 25 kg/ha; B @ 1 kg/ha)."
        ),
        "common_pests": (
            "1) Pod Borer (Helicoverpa armigera) — major pest; bores into pods; spray "
            "Bt formulations or Emamectin Benzoate 5% SG @ 200 g/ha at pod-formation. "
            "2) Aphids — colonize tender shoots; spray Imidacloprid or apply neem oil "
            "(3%). 3) Cutworms — damage seedlings; soil drench with Chlorpyrifos. "
            "4) Bruchids (storage) — drill into stored seeds; mix Deltamethrin dust or "
            "store in airtight containers; sun-dry to <9% moisture before storage."
        ),
        "common_diseases": (
            "1) Rust (Uromyces fabae) — orange-brown pustules on leaves and pods; use "
            "resistant varieties + spray Mancozeb @ 0.25% or Propiconazole. 2) Wilt "
            "(Fusarium oxysporum) — sudden wilting, vascular browning; use resistant "
            "varieties + Trichoderma seed treatment + crop rotation. 3) Ascochyta Blight — "
            "dark spots with concentric rings; spray Chlorothalonil. 4) Stemphylium "
            "Blight — yellow-brown spots; spray Mancozeb + Carbendazim. 5) Root Rot — "
            "improve drainage + Trichoderma application."
        ),
        "harvesting": (
            "Harvest when 75-80% of pods turn yellow-brown and seeds rattle inside. "
            "Don't wait for full maturity—pods shatter and shed seeds. Cut crop with "
            "sickle, bundle, and stack in field for 3-4 days drying. Thresh by trampling "
            "or with mechanical thresher. Winnow to clean seeds. Dry seeds to 9-10% "
            "moisture for safe storage."
        ),
        "average_yield": (
            "Traditional rainfed: 600-800 kg/ha. Improved varieties with good management: "
            "1200-1500 kg/ha. Irrigated best management: 2000-2500 kg/ha. World average: "
            "1000 kg/ha. Indian average: 760 kg/ha. Canada (world's largest exporter): "
            "1800 kg/ha. Plant Year-after-year rotation improves nitrogen-fixing efficiency."
        ),
        "nutritional_value": (
            "Excellent source of protein (25-30% by weight), much higher than cereals. "
            "Rich in iron (7-8 mg/100g), folate, dietary fiber, and B-vitamins. Low fat "
            "(<1%). Glycemic index low (~30)—suitable for diabetics. Combined with cereals "
            "provides complete protein. Daily consumption of 50-80 g recommended for "
            "balanced vegetarian diet."
        ),
    },

}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_all_documents():
    """
    Converts KNOWLEDGE_BASE into a list of (text, metadata) tuples
    for vector embedding and ChromaDB storage.
    """
    documents = []

    for crop_name, crop_data in KNOWLEDGE_BASE.items():
        for section, content in crop_data.items():
            if not isinstance(content, str):
                continue

            section_label = section.replace("_", " ").title()
            text = f"Crop: {crop_name.title()} | Topic: {section_label}\n\n{content}"

            metadata = {
                "crop": crop_name,
                "section": section,
                "scientific_name": crop_data.get("scientific_name", ""),
            }

            documents.append({"text": text, "metadata": metadata})

    return documents


def get_supported_crops():
    """Returns a list of crops covered in the knowledge base."""
    return list(KNOWLEDGE_BASE.keys())


if __name__ == "__main__":
    docs = get_all_documents()
    print(f"✅ Knowledge base loaded: {len(KNOWLEDGE_BASE)} crops, {len(docs)} document chunks")
    print(f"📚 Supported crops: {', '.join(get_supported_crops())}")