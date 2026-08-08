import pandas as pd
from pathlib import Path
import random
import json
from datetime import datetime, timedelta

def generate_verified_tech_dataset():
    raw_dir = Path(__file__).parent.parent / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    tech_items = [
        # --- SMARTPHONES (6) ---
        {
            "parent_asin": 1,
            "title": "Apple iPhone 15 Pro Max (256 GB) - Natural Titanium",
            "Brand": "Apple",
            "main_category": "Smartphones",
            "categories": "Smartphones|Apple|Flagship|5G",
            "description": "Apple iPhone 15 Pro Max with forged titanium design, Super Retina XDR OLED display, A17 Pro chip with 6-core GPU, 48MP main camera with 5x optical zoom telephoto, USB-C 3 speeds, and Action button.",
            "price": 149900,
            "Original_Price": 159900,
            "Discount": "6% OFF",
            "average_rating": 4.8,
            "rating_number": 1420,
            "store": "Apple Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "8GB RAM | 256GB Storage",
            "Processor": "A17 Pro Bionic Chip",
            "Camera_Specs": "48MP Main + 12MP Ultra-wide + 12MP 5x Telephoto",
            "Battery": "4422 mAh (Up to 29 hrs Video Playback)",
            "features": "Titanium Build|A17 Pro|48MP Camera|Dynamic Island|USB-C 3",
            "reviews": json.dumps([
                {"user": "Rohan Sharma", "rating": 5, "comment": "Unbelievable build quality and battery life! The 5x optical zoom is super sharp.", "date": "2026-07-15"},
                {"user": "Priya Patel", "rating": 5, "comment": "A17 Pro plays AAA games effortlessly. Titanium body feels premium yet light.", "date": "2026-07-28"}
            ])
        },
        {
            "parent_asin": 2,
            "title": "Samsung Galaxy S24 Ultra 5G (Titanium Gray, 12GB RAM, 512GB Storage)",
            "Brand": "Samsung",
            "main_category": "Smartphones",
            "categories": "Smartphones|Samsung|Flagship|Galaxy|AI",
            "description": "Samsung Galaxy S24 Ultra 5G powered by Galaxy AI, Snapdragon 8 Gen 3 for Galaxy, 200MP camera with Quad Tele system, Built-in S-Pen, Titanium Frame, and 6.8-inch QHD+ Dynamic AMOLED 2X display.",
            "price": 129999,
            "Original_Price": 144999,
            "Discount": "10% OFF",
            "average_rating": 4.7,
            "rating_number": 2150,
            "store": "Samsung India",
            "Image_URL": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "12GB RAM | 512GB Storage",
            "Processor": "Snapdragon 8 Gen 3 for Galaxy",
            "Camera_Specs": "200MP Main + 50MP Periscope + 12MP Ultra-wide + 10MP Telephoto",
            "Battery": "5000 mAh with 45W Super Fast Charging",
            "features": "Galaxy AI|200MP Quad Camera|S-Pen Included|Titanium Armor Frame",
            "reviews": json.dumps([
                {"user": "Vikram Singh", "rating": 5, "comment": "Galaxy AI features like Circle to Search and Live Translate are game changers!", "date": "2026-06-10"}
            ])
        },
        {
            "parent_asin": 3,
            "title": "OnePlus 12 5G (Silky Black, 16GB RAM, 512GB Storage)",
            "Brand": "OnePlus",
            "main_category": "Smartphones",
            "categories": "Smartphones|OnePlus|Flagship|Hasselblad",
            "description": "OnePlus 12 5G featuring 4th Gen Hasselblad Camera System for Mobile, Snapdragon 8 Gen 3 Mobile Platform, 2K 120 Hz ProXDR Display, and 5400 mAh Battery with 100W SUPERVOOC Charging.",
            "price": 69999,
            "Original_Price": 74999,
            "Discount": "7% OFF",
            "average_rating": 4.6,
            "rating_number": 3800,
            "store": "OnePlus Direct",
            "Image_URL": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "16GB RAM | 512GB Storage",
            "Processor": "Snapdragon 8 Gen 3",
            "Camera_Specs": "50MP Sony LYT-808 + 64MP Periscope + 48MP Ultra-wide Hasselblad",
            "Battery": "5400 mAh with 100W Wired & 50W AIRVOOC",
            "features": "Hasselblad Camera|100W SUPERVOOC|Snapdragon 8 Gen 3|2K 120Hz ProXDR",
            "reviews": json.dumps([
                {"user": "Amit Kumar", "rating": 5, "comment": "Charges from 1% to 100% in under 26 minutes! Super fast performance.", "date": "2026-07-12"}
            ])
        },
        {
            "parent_asin": 4,
            "title": "Google Pixel 8 Pro (Obsidian, 12GB RAM, 128GB Storage)",
            "Brand": "Google",
            "main_category": "Smartphones",
            "categories": "Smartphones|Google|Pixel|Camera|AI",
            "description": "Google Pixel 8 Pro powered by Google Tensor G3 with Google AI, fully upgraded pro triple cameras, Temperature sensor, Super Actua display, and 7 years of OS updates.",
            "price": 99999,
            "Original_Price": 106999,
            "Discount": "7% OFF",
            "average_rating": 4.5,
            "rating_number": 980,
            "store": "Google Store India",
            "Image_URL": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "12GB RAM | 128GB Storage",
            "Processor": "Google Tensor G3",
            "Camera_Specs": "50MP Main + 48MP Ultra-wide + 48MP 5x Telephoto",
            "Battery": "5050 mAh with 30W Fast Charging",
            "features": "Tensor G3|Best AI Photography|Best Take|7 Years Updates",
            "reviews": json.dumps([
                {"user": "Sanjay Rao", "rating": 5, "comment": "Best camera algorithms on any phone. Skin tones look natural.", "date": "2026-06-20"}
            ])
        },
        {
            "parent_asin": 5,
            "title": "Nothing Phone (2a) 5G (Black, 8GB RAM, 128GB Storage)",
            "Brand": "Nothing",
            "main_category": "Smartphones",
            "categories": "Smartphones|Nothing|Budget|Glyph",
            "description": "Nothing Phone (2a) 5G with iconic Glyph Interface, MediaTek Dimensity 7200 Pro processor, 50 MP dual rear camera with OIS, 120Hz flexible AMOLED display, and Clean Nothing OS 2.5.",
            "price": 23999,
            "Original_Price": 25999,
            "Discount": "8% OFF",
            "average_rating": 4.4,
            "rating_number": 5200,
            "store": "Nothing Official",
            "Image_URL": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "8GB RAM | 128GB Storage",
            "Processor": "Dimensity 7200 Pro",
            "Camera_Specs": "50MP OIS Main + 50MP Ultra-wide",
            "Battery": "5000 mAh with 45W Fast Charging",
            "features": "Glyph Interface|Clean OS|50MP Dual OIS Camera|120Hz AMOLED",
            "reviews": json.dumps([
                {"user": "Karan Malhotra", "rating": 5, "comment": "Unique transparent design and glyph lights turn heads everywhere!", "date": "2026-07-22"}
            ])
        },
        {
            "parent_asin": 6,
            "title": "Xiaomi Redmi Note 13 Pro+ 5G (Fusion Purple, 12GB RAM, 256GB Storage)",
            "Brand": "Xiaomi",
            "main_category": "Smartphones",
            "categories": "Smartphones|Xiaomi|Redmi|Camera",
            "description": "Xiaomi Redmi Note 13 Pro+ 5G with 3D Curved 1.5K 120Hz AMOLED Display, 200MP OIS Camera with 4x lossless zoom, IP68 Water & Dust Resistance, and 120W HyperCharge.",
            "price": 31999,
            "Original_Price": 35999,
            "Discount": "11% OFF",
            "average_rating": 4.3,
            "rating_number": 8400,
            "store": "Xiaomi India",
            "Image_URL": "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "12GB RAM | 256GB Storage",
            "Processor": "Dimensity 7200-Ultra",
            "Camera_Specs": "200MP OIS Main + 8MP Ultra-wide + 2MP Macro",
            "Battery": "5000 mAh with 120W HyperCharge",
            "features": "200MP OIS Camera|120W Charging|3D Curved Display|IP68",
            "reviews": json.dumps([
                {"user": "Deepak Joshi", "rating": 4, "comment": "Curved screen looks premium like a 70k phone.", "date": "2026-07-05"}
            ])
        },

        # --- GAMING DESKTOP PCS & LAPTOPS (8) ---
        {
            "parent_asin": 7,
            "title": "ASUS ROG Strix G16 Gaming Desktop PC (Intel Core i9-14900KF, RTX 4080 Super 16GB, 32GB DDR5, 2TB SSD, Liquid Cooled)",
            "Brand": "ASUS",
            "main_category": "Laptops & PCs",
            "categories": "Laptops & PCs|ASUS|ROG|GamingPC|Desktop|RTX4080",
            "description": "ASUS ROG Strix G16 flagship gaming desktop computer powered by 14th Gen Intel Core i9-14900KF processor, NVIDIA GeForce RTX 4080 Super 16GB GDDR6X GPU, 32GB DDR5 RAM, 2TB PCIe 4.0 NVMe SSD, 240mm liquid cooling system, and Aura Sync RGB glass side panel.",
            "price": 289990,
            "Original_Price": 319990,
            "Discount": "9% OFF",
            "average_rating": 4.9,
            "rating_number": 340,
            "store": "ASUS ROG Store",
            "Image_URL": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "32GB DDR5 RAM | 2TB PCIe 4.0 NVMe SSD",
            "Processor": "14th Gen Intel Core i9-14900KF (24 Cores / 5.8GHz)",
            "Camera_Specs": "N/A (Desktop Tower)",
            "Battery": "850W 80 Gold Power Supply Unit",
            "features": "RTX 4080 Super 16GB|Liquid Cooled i9-14900KF|Tempered Glass RGB Case|Wi-Fi 6E",
            "reviews": json.dumps([
                {"user": "Yash Pal", "rating": 5, "comment": "Absolute monster PC! Runs Cyberpunk 2077 at 4K Ultra Ray Tracing at 120+ FPS easily.", "date": "2026-07-29"}
            ])
        },
        {
            "parent_asin": 8,
            "title": "HP OMEN 45L Gaming Desktop PC (AMD Ryzen 9 7900X, RTX 4070 Ti Super 16GB, 32GB DDR5 RAM, 1TB NVMe SSD)",
            "Brand": "HP",
            "main_category": "Laptops & PCs",
            "categories": "Laptops & PCs|HP|OMEN|GamingPC|Desktop|RTX4070Ti",
            "description": "HP OMEN 45L Gaming Desktop with revolutionary Cryo Chamber cooling system, AMD Ryzen 9 7900X 12-core CPU, NVIDIA GeForce RTX 4070 Ti Super 16GB, 32GB Kingston FURY DDR5 RGB memory, and 1TB WD Black PCIe SSD.",
            "price": 234990,
            "Original_Price": 259990,
            "Discount": "10% OFF",
            "average_rating": 4.8,
            "rating_number": 290,
            "store": "HP Store India",
            "Image_URL": "https://images.unsplash.com/photo-1593640408182-31c70c8268f5?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "32GB Kingston FURY DDR5 RAM | 1TB M.2 SSD",
            "Processor": "AMD Ryzen 9 7900X (12 Cores / 24 Threads)",
            "Camera_Specs": "N/A (Desktop Tower)",
            "Battery": "800W 80 Plus Gold PSU",
            "features": "OMEN Cryo Chamber|RTX 4070 Ti Super|Tool-less Glass Case|Kingston RGB RAM",
            "reviews": json.dumps([
                {"user": "Harish Chandra", "rating": 5, "comment": "Patented Cryo Chamber keeps CPU temperatures under 65 degrees even on heavy rendering loads.", "date": "2026-07-11"}
            ])
        },
        {
            "parent_asin": 9,
            "title": "Apple MacBook Air 15-inch M3 Chip (16GB RAM, 512GB SSD) - Starlight",
            "Brand": "Apple",
            "main_category": "Laptops & PCs",
            "categories": "Laptops & PCs|Apple|MacBook|Ultrabook|M3",
            "description": "Apple MacBook Air 15-inch with M3 chip, 8-core CPU and 10-core GPU, Liquid Retina display, 1080p FaceTime HD camera, MagSafe 3 charging, and up to 18 hours of battery life.",
            "price": 154900,
            "Original_Price": 164900,
            "Discount": "6% OFF",
            "average_rating": 4.9,
            "rating_number": 890,
            "store": "Apple Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "16GB Unified Memory | 512GB SSD",
            "Processor": "Apple M3 Chip (8-Core CPU / 10-Core GPU)",
            "Camera_Specs": "1080p FaceTime HD Camera",
            "Battery": "Up to 18 Hours Battery Life",
            "features": "M3 Chip|15.3-inch Liquid Retina Display|Fanless Silent Design|MagSafe 3",
            "reviews": json.dumps([
                {"user": "Ananya Nair", "rating": 5, "comment": "Dead silent, blazing fast for video editing, and battery lasts 2 full workdays!", "date": "2026-06-18"}
            ])
        },
        {
            "parent_asin": 10,
            "title": "ASUS ROG Zephyrus G16 Gaming Laptop (16-inch 240Hz OLED, Intel Core Ultra 9, RTX 4070 8GB, 32GB RAM, 1TB SSD)",
            "Brand": "ASUS",
            "main_category": "Laptops & PCs",
            "categories": "Laptops & PCs|ASUS|ROG|Gaming|RTX4070",
            "description": "ASUS ROG Zephyrus G16 AI Gaming Laptop featuring 2.5K 240Hz ROG Nebula OLED display, Intel Core Ultra 9 185H processor, NVIDIA GeForce RTX 4070 GPU, CNC Aluminum chassis, and ROG Intelligent Cooling.",
            "price": 219990,
            "Original_Price": 249990,
            "Discount": "12% OFF",
            "average_rating": 4.8,
            "rating_number": 420,
            "store": "ASUS ROG Store",
            "Image_URL": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "32GB LPDDR5X RAM | 1TB PCIe 4.0 SSD",
            "Processor": "Intel Core Ultra 9 185H (16 Cores / NPU AI)",
            "Camera_Specs": "1080p FHD IR Camera with Windows Hello",
            "Battery": "90Wh Battery with 100W USB-C PD Charging",
            "features": "240Hz OLED Display|RTX 4070 8GB|CNC Aluminum|Tri-Fan Cooling",
            "reviews": json.dumps([
                {"user": "Rahul Verma", "rating": 5, "comment": "OLED screen colors are breathtaking and Cyberpunk 2077 runs smooth at 90+ FPS!", "date": "2026-07-14"}
            ])
        },
        {
            "parent_asin": 11,
            "title": "Dell XPS 13 Laptop (Intel Core Ultra 7 155H, 13.4-inch 3K+ Touch OLED, 16GB RAM, 512GB SSD)",
            "Brand": "Dell",
            "main_category": "Laptops & PCs",
            "categories": "Laptops & PCs|Dell|XPS|Ultrabook|OLED",
            "description": "Dell XPS 13 premium ultraportable laptop crafted with CNC machined aluminum, capacitive touch function row, seamless glass touchpad, InfinityEdge 3K+ OLED touchscreen, and Dolby Atmos audio.",
            "price": 144990,
            "Original_Price": 159990,
            "Discount": "9% OFF",
            "average_rating": 4.6,
            "rating_number": 610,
            "store": "Dell Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "16GB RAM | 512GB NVMe SSD",
            "Processor": "Intel Core Ultra 7 155H",
            "Camera_Specs": "FHD 1080p Web Camera",
            "Battery": "55Whr Battery with Fast Charge",
            "features": "InfinityEdge 3K+ OLED Touch|CNC Aluminum|Glass Touchpad|Dolby Atmos",
            "reviews": json.dumps([
                {"user": "Meera Sen", "rating": 4, "comment": "Minimalist futuristic design. Touchpad takes 1 day to get used to.", "date": "2026-06-25"}
            ])
        },

        # --- CAMERAS & PHOTOGRAPHY (7) ---
        {
            "parent_asin": 12,
            "title": "Sony Alpha 7 IV Full-Frame Mirrorless Camera Body (33MP, 4K 60p, Real-Time Eye AF, 5-Axis OIS)",
            "Brand": "Sony",
            "main_category": "Cameras",
            "categories": "Cameras|Sony|Alpha|Mirrorless|Full-Frame",
            "description": "Sony Alpha 7 IV full-frame mirrorless camera featuring 33MP Exmor R CMOS sensor, BIONZ XR processing engine, 4K 60p 10-bit 4:2:2 video, 759-point AF with Real-time Eye AF for Humans/Animals/Birds.",
            "price": 214990,
            "Original_Price": 229990,
            "Discount": "7% OFF",
            "average_rating": 4.9,
            "rating_number": 1150,
            "store": "Sony Center India",
            "Image_URL": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Dual SD/CFexpress Type A Slots",
            "Processor": "BIONZ XR Image Processor",
            "Camera_Specs": "33MP Full-Frame Exmor R Sensor | 4K 60p 10-bit 4:2:2",
            "Battery": "NP-FZ100 Rechargeable Battery (580 shots)",
            "features": "33MP Full-Frame|4K 60p Video|Real-Time Eye AF|5-Axis In-Body Stabilization",
            "reviews": json.dumps([
                {"user": "Manish Kulkarni", "rating": 5, "comment": "Gold standard hybrid camera for weddings and commercial video shoots.", "date": "2026-07-01"}
            ])
        },
        {
            "parent_asin": 13,
            "title": "Sony ZV-E10 Mirrorless Vlog Camera (24.2MP, 4K Video, Vari-Angle Touchscreen, Directional 3-Capsule Mic)",
            "Brand": "Sony",
            "main_category": "Cameras",
            "categories": "Cameras|Sony|Alpha|Vlog|Mirrorless|Budget",
            "description": "Sony ZV-E10 APS-C interchangeable lens mirrorless vlogging camera featuring 24.2MP Exmor CMOS sensor, 4K HDR video recording, Product Showcase setting, Background Defocus button, and 3-Capsule Mic with windscreen.",
            "price": 47990,
            "Original_Price": 52990,
            "Discount": "9% OFF",
            "average_rating": 4.7,
            "rating_number": 3420,
            "store": "Sony Center India",
            "Image_URL": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Single SD UHS-I Card Slot",
            "Processor": "BIONZ X Image Processor",
            "Camera_Specs": "24.2MP APS-C Exmor CMOS | 4K 30p 100Mbps Video",
            "Battery": "NP-FW50 Battery (440 shots / 80 min video)",
            "features": "24.2MP Sensor|Vari-Angle Screen|Product Showcase|Background Defocus",
            "reviews": json.dumps([
                {"user": "Siddharth Verma", "rating": 5, "comment": "Best vlogging camera under 50k! Product showcase mode switches focus instantly.", "date": "2026-07-19"}
            ])
        },
        {
            "parent_asin": 14,
            "title": "Canon EOS R50 Mirrorless Camera Body (24.2MP, 4K 30p Uncropped, Dual Pixel CMOS AF II, OLED EVF)",
            "Brand": "Canon",
            "main_category": "Cameras",
            "categories": "Cameras|Canon|EOS|Mirrorless|Compact|Budget",
            "description": "Canon EOS R50 compact lightweight mirrorless camera featuring 24.2MP APS-C CMOS sensor, DIGIC X processor, Dual Pixel CMOS AF II with subject detection, 4K 30p uncropped video, and 15 fps electronic burst.",
            "price": 49990,
            "Original_Price": 54990,
            "Discount": "9% OFF",
            "average_rating": 4.8,
            "rating_number": 1850,
            "store": "Canon India",
            "Image_URL": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Single SD UHS-I Card Slot",
            "Processor": "DIGIC X Image Processor",
            "Camera_Specs": "24.2MP APS-C CMOS | 4K 30p Uncropped | 6K Oversampled",
            "Battery": "LP-E17 Rechargeable Li-ion",
            "features": "24.2MP Sensor|Dual Pixel AF II|Compact 375g Body|4K 30p",
            "reviews": json.dumps([
                {"user": "Akash Deshmukh", "rating": 5, "comment": "Super sharp 4K video and animal eye tracking works brilliantly.", "date": "2026-07-10"}
            ])
        },
        {
            "parent_asin": 15,
            "title": "GoPro HERO12 Black Waterproof Action Camera (5.3K60 Video, 27MP Photos, HDR, HyperSmooth 6.0)",
            "Brand": "GoPro",
            "main_category": "Cameras",
            "categories": "Cameras|GoPro|Action|Waterproof|5.3K",
            "description": "GoPro HERO12 Black waterproof action camera featuring 5.3K60 and 4K120 video, 27MP photos, Emmy Award-winning HyperSmooth 6.0 video stabilization, HDR video, Bluetooth audio support, and dual LCD screens.",
            "price": 37990,
            "Original_Price": 45000,
            "Discount": "16% OFF",
            "average_rating": 4.7,
            "rating_number": 6200,
            "store": "GoPro Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "MicroSD Slot (Up to 512GB)",
            "Processor": "GP2 Image Processor",
            "Camera_Specs": "27MP 1/1.9-inch Sensor | 5.3K 60fps / 4K 120fps",
            "Battery": "1720 mAh Enduro Battery (70 min 5.3K)",
            "features": "5.3K60 Video|HyperSmooth 6.0 Stabilization|Waterproof 33ft|HDR Video",
            "reviews": json.dumps([
                {"user": "Nikhil Motovlog", "rating": 5, "comment": "HyperSmooth 6.0 stabilization makes bumpy bike rides look like a Hollywood drone shot!", "date": "2026-07-25"}
            ])
        },
        {
            "parent_asin": 16,
            "title": "Fujifilm X-T5 Mirrorless Camera Body (40.2MP APS-C X-Trans CMOS 5 HR Sensor, 6.2K Video, Silver)",
            "Brand": "Fujifilm",
            "main_category": "Cameras",
            "categories": "Cameras|Fujifilm|APS-C|Retro|FilmSimulation",
            "description": "Fujifilm X-T5 photography-first mirrorless camera featuring 40.2MP X-Trans 5 HR sensor, X-Processor 5, 19 Film Simulation modes, 7-stop IBIS, 3-way tilting LCD, and classic analog control dials.",
            "price": 169990,
            "Original_Price": 184990,
            "Discount": "8% OFF",
            "average_rating": 4.9,
            "rating_number": 510,
            "store": "Fujifilm Store",
            "Image_URL": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Dual SD UHS-II Slots",
            "Processor": "X-Processor 5 Engine",
            "Camera_Specs": "40.2MP X-Trans CMOS 5 HR | 6.2K 30p 10-bit Video",
            "Battery": "NP-W235 Battery (Up to 700 frames)",
            "features": "40.2MP High-Res Sensor|19 Film Simulations|Classic Dial Controls|7-stop IBIS",
            "reviews": json.dumps([
                {"user": "Arjun Saxena", "rating": 5, "comment": "Film simulations produce SOOC JPEGs that need zero color grading.", "date": "2026-07-21"}
            ])
        },

        # --- AUDIO & HEADPHONES (4) ---
        {
            "parent_asin": 15,
            "title": "Sony WH-1000XM5 Wireless Premium Noise Canceling Headphones (Silver, 30 Hr Battery, Auto NC Optimizer)",
            "Brand": "Sony",
            "main_category": "Audio",
            "categories": "Audio|Sony|Headphones|ANC|Wireless",
            "description": "Sony WH-1000XM5 industry-leading noise canceling headphones with two processors and 8 microphones, Auto NC Optimizer, Speak-to-Chat technology, 30-hour battery life, and ultra-comfortable lightweight design.",
            "price": 29990,
            "Original_Price": 34990,
            "Discount": "14% OFF",
            "average_rating": 4.7,
            "rating_number": 6800,
            "store": "Sony Official",
            "Image_URL": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Bluetooth 5.2 / LDAC / AAC",
            "Processor": "Processor V1 + HD Noise Canceling Processor QN1",
            "Camera_Specs": "4 Beamforming Mics for Calls",
            "Battery": "30 Hours Battery (3 min Charge = 3 Hours)",
            "features": "Industry-leading ANC|30-Hour Battery|Multipoint Bluetooth|LDAC High-Res Audio",
            "reviews": json.dumps([
                {"user": "Gautam Sethi", "rating": 5, "comment": "Cancels out airplane engine noise completely. Super comfy soft leather cups.", "date": "2026-06-19"}
            ])
        },
        {
            "parent_asin": 16,
            "title": "Apple AirPods Pro (2nd Generation) with MagSafe Case (USB-C) - Active Noise Cancellation & Adaptive Audio",
            "Brand": "Apple",
            "main_category": "Audio",
            "categories": "Audio|Apple|AirPods|Earbuds|ANC",
            "description": "Apple AirPods Pro 2nd Gen featuring H2 chip, up to 2x more Active Noise Cancellation, Adaptive Audio, Transparency mode, Personalized Spatial Audio with dynamic head tracking, and USB-C MagSafe Charging Case.",
            "price": 23900,
            "Original_Price": 24900,
            "Discount": "4% OFF",
            "average_rating": 4.8,
            "rating_number": 9500,
            "store": "Apple Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Bluetooth 5.3 / Apple H2 Chip",
            "Processor": "Apple H2 Headphone Chip",
            "Camera_Specs": "Dual Beamforming Mics",
            "Battery": "6 Hours Earbud (30 Hours Total with USB-C Case)",
            "features": "Apple H2 Chip|2x Noise Cancellation|Adaptive Audio|MagSafe USB-C Case",
            "reviews": json.dumps([
                {"user": "Rhea Menon", "rating": 5, "comment": "Seamless switching between iPhone and MacBook.", "date": "2026-07-11"}
            ])
        },

        # --- GAMING MONITORS, MICE & KEYBOARDS (6) ---
        {
            "parent_asin": 17,
            "title": "Samsung Odyssey OLED G8 34-inch UWQHD Curved Gaming Monitor (175Hz, 0.03ms, Neo Quantum Processor, Smart TV)",
            "Brand": "Samsung",
            "main_category": "Gaming & Peripherals",
            "categories": "Gaming & Peripherals|Samsung|Monitor|OLED|175Hz|Curved",
            "description": "Samsung Odyssey OLED G8 34-inch Ultra-WQHD (3440 x 1440) 1800R curved gaming monitor featuring Quantum Dot OLED technology, 175Hz refresh rate, 0.03ms response time, VESA DisplayHDR True Black 400, Gaming Hub, and Slim Metal Design.",
            "price": 99990,
            "Original_Price": 119990,
            "Discount": "17% OFF",
            "average_rating": 4.9,
            "rating_number": 680,
            "store": "Samsung Direct",
            "Image_URL": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "34-inch 21:9 UWQHD QD-OLED Panel",
            "Processor": "Neo Quantum Processor O",
            "Camera_Specs": "N/A (Gaming Monitor)",
            "Battery": "AC Powered (65W USB-C PD Output)",
            "features": "34-inch QD-OLED 175Hz|0.03ms Response|1800R Curve|Neo Quantum Engine",
            "reviews": json.dumps([
                {"user": "Varun Taneja", "rating": 5, "comment": "Infinite contrast ratio and true blacks make games look unreal! Best monitor I've ever owned.", "date": "2026-07-28"}
            ])
        },
        {
            "parent_asin": 18,
            "title": "LG UltraGear 27-inch 240Hz QHD Gaming Monitor (Nano IPS 1ms, HDR10, G-SYNC Compatible, HDMI 2.1)",
            "Brand": "LG",
            "main_category": "Gaming & Peripherals",
            "categories": "Gaming & Peripherals|LG|Monitor|240Hz|QHD|NanoIPS",
            "description": "LG UltraGear 27GR83Q 27-inch QHD (2560 x 1440) esports gaming monitor featuring Nano IPS panel, 240Hz refresh rate, 1ms (GtG) response time, NVIDIA G-SYNC & AMD FreeSync Premium Pro, and HDMI 2.1 VRR support.",
            "price": 38990,
            "Original_Price": 45000,
            "Discount": "13% OFF",
            "average_rating": 4.7,
            "rating_number": 1420,
            "store": "LG Electronics India",
            "Image_URL": "https://images.unsplash.com/photo-1547082299-de196ea013d6?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "27-inch QHD (2560x1440) Nano IPS",
            "Processor": "NVIDIA G-SYNC Compatible Engine",
            "Camera_Specs": "N/A (Gaming Monitor)",
            "Battery": "AC Powered",
            "features": "240Hz Refresh Rate|Nano IPS 1ms GtG|HDMI 2.1 VRR|Height & Tilt Stand",
            "reviews": json.dumps([
                {"user": "Shubham Gill", "rating": 5, "comment": "240Hz at 1440p resolution is the sweet spot for competitive shooter games.", "date": "2026-07-16"}
            ])
        },
        {
            "parent_asin": 19,
            "title": "Logitech G Pro X Superlight 2 Wireless Gaming Mouse (60g Ultra-Light, HERO 2 Sensor, 32K DPI, Black)",
            "Brand": "Logitech",
            "main_category": "Gaming & Peripherals",
            "categories": "Gaming & Peripherals|Logitech|Mouse|Wireless|Esports",
            "description": "Logitech G Pro X Superlight 2 Lightspeed wireless gaming mouse engineered with top esports pros. Features 60-gram ultra-lightweight design, HERO 2 sensor with 32,000 DPI, LIGHTFORCE hybrid switches, and 95-hour battery life.",
            "price": 13995,
            "Original_Price": 15995,
            "Discount": "13% OFF",
            "average_rating": 4.9,
            "rating_number": 3100,
            "store": "Logitech G Store",
            "Image_URL": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Onboard Memory Profiles",
            "Processor": "Logitech HERO 2 Sensor (32,000 DPI)",
            "Camera_Specs": "N/A",
            "Battery": "95 Hours Constant Motion Battery Life",
            "features": "60g Ultra Lightweight|32K DPI HERO 2 Sensor|LIGHTFORCE Hybrid Switches|95h Battery",
            "reviews": json.dumps([
                {"user": "Chetan FPS", "rating": 5, "comment": "Flicks in CS2 feel effortless thanks to the 60g weight and zero wireless latency.", "date": "2026-07-23"}
            ])
        },
        {
            "parent_asin": 20,
            "title": "Razer BlackWidow V4 Pro Mechanical Gaming Keyboard (Green Clicky Switches, Chroma RGB, Command Dial)",
            "Brand": "Razer",
            "main_category": "Gaming & Peripherals",
            "categories": "Gaming & Peripherals|Razer|Keyboard|Mechanical|RGB",
            "description": "Razer BlackWidow V4 Pro full-size mechanical gaming keyboard featuring Razer Green tactile clicky switches, Razer Command Dial, 8 dedicated macro keys, 8000Hz polling rate, plush magnetic wrist rest, and per-key Chroma RGB.",
            "price": 22999,
            "Original_Price": 25999,
            "Discount": "12% OFF",
            "average_rating": 4.7,
            "rating_number": 1450,
            "store": "Razer Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Hybrid On-Board & Cloud Storage",
            "Processor": "Razer HyperPolling 8000Hz Engine",
            "Camera_Specs": "N/A",
            "Battery": "USB-C Detachable Braided Cable",
            "features": "Razer Green Mechanical Switches|Command Dial|8 Macro Keys|Chroma RGB Underglow",
            "reviews": json.dumps([
                {"user": "Deepanshu Bansal", "rating": 5, "comment": "Tactile clicky feedback is super satisfying. Command dial is great for volume.", "date": "2026-07-04"}
            ])
        },
        {
            "parent_asin": 21,
            "title": "HyperX Cloud III Wireless Gaming Headset (53mm Angled Drivers, 120 Hour Battery, DTS Spatial Audio, 10mm Mic)",
            "Brand": "HyperX",
            "main_category": "Gaming & Peripherals",
            "categories": "Gaming & Peripherals|HyperX|Headset|Wireless|Gaming",
            "description": "HyperX Cloud III Wireless Gaming Headset featuring re-engineered 53mm angled drivers, signature memory foam comfort, ultra-clear 10mm noise-canceling mic, DTS Headphone:X Spatial Audio, and up to 120 hours of battery life.",
            "price": 12990,
            "Original_Price": 15990,
            "Discount": "19% OFF",
            "average_rating": 4.8,
            "rating_number": 2890,
            "store": "HyperX Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1599669454699-24889d6df33b?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "2.4GHz Wireless USB-C Dongle",
            "Processor": "DTS Headphone:X Spatial Audio DSP",
            "Camera_Specs": "10mm Ultra-Clear Noise-Canceling Mic",
            "Battery": "120 Hours Continuous Battery Life",
            "features": "120 Hour Battery|53mm Angled Drivers|Memory Foam Comfort|DTS 3D Spatial Audio",
            "reviews": json.dumps([
                {"user": "Aman Shrivastav", "rating": 5, "comment": "120 hours battery means charging only once a month. Mic quality is crystal clear.", "date": "2026-07-17"}
            ])
        },
        {
            "parent_asin": 22,
            "title": "Sony PlayStation 5 Console (Slim Disc Edition, 1TB SSD, DualSense Wireless Controller)",
            "Brand": "Sony",
            "main_category": "Gaming & Peripherals",
            "categories": "Gaming & Peripherals|Sony|PS5|Console|4K120",
            "description": "Sony PlayStation 5 (PS5 Slim Disc Edition) gaming console featuring 1TB high-speed SSD, Tempest 3D AudioTech, ray tracing, 4K 120Hz HDR output, and DualSense wireless controller with haptic feedback & adaptive triggers.",
            "price": 54990,
            "Original_Price": 54990,
            "Discount": "0%",
            "average_rating": 4.9,
            "rating_number": 8900,
            "store": "Sony Center India",
            "Image_URL": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "16GB GDDR6 RAM | 1TB Custom SSD",
            "Processor": "AMD Zen 2 8-Core CPU / RDNA 2 GPU",
            "Camera_Specs": "N/A",
            "Battery": "AC Mains Powered",
            "features": "1TB High Speed SSD|Ray Tracing 4K 120Hz|DualSense Haptics|Tempest 3D Audio",
            "reviews": json.dumps([
                {"user": "Siddharth Das", "rating": 5, "comment": "Spider-Man 2 and God of War Ragnarok load in 2 seconds flat! Mindblowing console.", "date": "2026-07-20"}
            ])
        },

        # --- CHARGERS & CABLES (4) ---
        {
            "parent_asin": 23,
            "title": "Anker Prime 67W GaN Fast Wall Charger (3-Port USB-C & USB-A Power Adapter)",
            "Brand": "Anker",
            "main_category": "Chargers & Cables",
            "categories": "Chargers & Cables|Anker|FastCharger|GaN|USB-C",
            "description": "Anker Prime 67W GaN 3-port fast wall charger with GaNPrime technology, ActiveShield 2.0 safety protection, foldable plug, capable of fast charging MacBook Pro, iPhone 15, iPad, and Samsung Galaxy simultaneously.",
            "price": 3999,
            "Original_Price": 4999,
            "Discount": "20% OFF",
            "average_rating": 4.6,
            "rating_number": 4100,
            "store": "Anker Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "Dual USB-C + Single USB-A Port",
            "Processor": "GaNPrime Tech + ActiveShield 2.0",
            "Camera_Specs": "N/A",
            "Battery": "67W Ultra-Fast Power Delivery Output",
            "features": "67W Fast Charging|GaN Tech|Compact Foldable Plug|Triple Device Charge",
            "reviews": json.dumps([
                {"user": "Tarun Jha", "rating": 5, "comment": "Replaced 3 brick chargers in my laptop bag with this tiny 67W adapter!", "date": "2026-07-13"}
            ])
        },
        {
            "parent_asin": 24,
            "title": "Anker 100W USB-C to USB-C Heavy-Duty Nylon Braided Cable (6ft / 1.8m)",
            "Brand": "Anker",
            "main_category": "Chargers & Cables",
            "categories": "Chargers & Cables|Anker|USB-C|100W|Braided",
            "description": "Anker 100W 6ft double-braided nylon USB-C to USB-C charging cable with E-Marker chip, supporting Power Delivery fast charging up to 100W for MacBook Pro, Dell XPS, iPad Pro, and Galaxy S24.",
            "price": 1299,
            "Original_Price": 1699,
            "Discount": "24% OFF",
            "average_rating": 4.7,
            "rating_number": 12800,
            "store": "Anker Direct",
            "Image_URL": "https://images.unsplash.com/photo-1616440342855-468f3ae908c6?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "6ft / 1.8 Meter Length",
            "Processor": "Smart E-Marker Chip",
            "Camera_Specs": "N/A",
            "Battery": "Supports Up to 100W Power Delivery",
            "features": "100W Power Delivery|Heavy Duty Braided Nylon|E-Marker Chip|35,000+ Bend Lifespan",
            "reviews": json.dumps([
                {"user": "Rajesh Sen", "rating": 5, "comment": "Indestructible cable. Replaced my broken stock cable.", "date": "2026-07-18"}
            ])
        },

        # --- SMARTWATCHES (2) ---
        {
            "parent_asin": 25,
            "title": "Apple Watch Series 9 GPS 45mm (Midnight Aluminum Case with Midnight Sport Band)",
            "Brand": "Apple",
            "main_category": "Smartwatches",
            "categories": "Smartwatches|Apple|AppleWatch|Fitness|S9",
            "description": "Apple Watch Series 9 powered by S9 SiP chip, magical Double Tap gesture control, brighter 2000 nits Always-On Retina display, ECG app, Blood Oxygen sensor, Advanced Workout metrics, and Fall Detection.",
            "price": 44900,
            "Original_Price": 44900,
            "Discount": "0%",
            "average_rating": 4.8,
            "rating_number": 3200,
            "store": "Apple Official Store",
            "Image_URL": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "64GB Internal Storage",
            "Processor": "Apple S9 SiP Dual-Core Processor",
            "Camera_Specs": "N/A",
            "Battery": "Up to 18 Hours (36 Hours in Low Power Mode)",
            "features": "S9 Chip|Double Tap Gesture|2000 nits Display|ECG & Blood Oxygen",
            "reviews": json.dumps([
                {"user": "Divya Kapoor", "rating": 5, "comment": "Double tap gesture to answer calls while holding coffee is so convenient!", "date": "2026-06-22"}
            ])
        },
        {
            "parent_asin": 26,
            "title": "Samsung Galaxy Watch 6 Classic LTE 47mm (Black, Rotating Bezel, Sapphire Crystal Glass)",
            "Brand": "Samsung",
            "main_category": "Smartwatches",
            "categories": "Smartwatches|Samsung|GalaxyWatch|LTE|Android",
            "description": "Samsung Galaxy Watch 6 Classic LTE featuring iconic physical rotating bezel, Sapphire Crystal glass display, Exynos W930 dual-core processor, BIA Body Composition sensor, Sleep Coaching, and 5ATM/IP68 water resistance.",
            "price": 36999,
            "Original_Price": 43999,
            "Discount": "16% OFF",
            "average_rating": 4.6,
            "rating_number": 2100,
            "store": "Samsung Direct",
            "Image_URL": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=800&auto=format&fit=crop&q=80",
            "Ram_Storage": "2GB RAM | 16GB Storage",
            "Processor": "Exynos W930 Dual-Core 1.4GHz",
            "Camera_Specs": "N/A",
            "Battery": "425 mAh with Fast Wireless Charging",
            "features": "Iconic Rotating Bezel|LTE Connectivity|Body Composition BIA|Sapphire Crystal Glass",
            "reviews": json.dumps([
                {"user": "Harsh Vardhan", "rating": 5, "comment": "Physical rotating bezel is satisfying to click. Great Wear OS app support.", "date": "2026-07-03"}
            ])
        }
    ]

    product_df = pd.DataFrame(tech_items)
    product_df.to_csv(raw_dir / "Product_Information_Dataset.csv", index=False)
    print(f"Generated {len(product_df)} Verified Product CSV in INR (Rs.).")

    # Generate Order Dataset
    customer_ids = [37077, 45120, 89102, 12044, 37077, 37077, 98201]
    priorities = ["High", "Medium", "High", "Low", "High", "Medium", "High"]
    payment_methods = ["UPI / GPay", "Credit Card", "NetBanking", "COD", "UPI / PhonePe", "EMI", "Debit Card"]
    genders = ["Male", "Female", "Male", "Female", "Male", "Female", "Male"]
    devices = ["Android App", "iOS App", "Mobile Web", "Desktop Web", "Android App", "iOS App", "Desktop Web"]

    orders = []
    base_date = datetime.now() - timedelta(days=60)
    for i in range(1, 35):
        item = random.choice(tech_items)
        cust_id = random.choice(customer_ids)
        prio = random.choice(priorities)
        dt = base_date + timedelta(days=i*1.5, hours=random.randint(1, 10))
        sales = item["price"]
        shipping = random.choice([0, 199, 299, 499])
        discount = random.randint(500, 3000)

        orders.append({
            "Order_ID": 4000 + i,
            "Order_Date": dt.strftime("%Y-%m-%d"),
            "Time": dt.strftime("%H:%M:%S"),
            "Customer_Id": cust_id,
            "Gender": random.choice(genders),
            "Device_Type": random.choice(devices),
            "Customer_Login_type": "Verified Member",
            "Product_Category": item["main_category"],
            "Product": item["title"],
            "Quantity": 1,
            "Sales": sales,
            "Discount": discount,
            "Profit": int(sales * 0.12),
            "Shipping_Cost": shipping,
            "Order_Priority": prio,
            "Payment_method": random.choice(payment_methods)
        })

    order_df = pd.DataFrame(orders)
    order_df.to_csv(raw_dir / "Order_Data_Dataset.csv", index=False)
    print(f"Generated Order CSV with {len(order_df)} records in INR (Rs.).")

if __name__ == "__main__":
    generate_verified_tech_dataset()
