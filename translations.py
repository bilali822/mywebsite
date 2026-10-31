"""All bilingual copy lives here. Edit, reload, done."""

UI = {
    "en": {
        "kicker": "Independent builder · Tripoli, Lebanon",
        "hero_title": "I build software in days. AI is the leverage — not the point.",
        "hero_lede": "Mohamed Belali. I take ideas from a note to a working product, usually before the scope doc gets written. I focus on shipping real solutions fast, keeping the process lean.",
        "cta_work": "Selected work",
        "nav_work": "Work",
        "nav_about": "About",
        "nav_contact": "Contact",
        "work_title": "Selected work",
        "work_intro": "Three projects, shipped between 2023 and 2024. Each was scoped, built, and maintained by one person. Ship times are listed because they're the point, not a flex.",
        "about_label": "About",
        "about_p1": "I've been building software for about four years, mostly for small businesses around the Levant that don't have a dev team and don't want to hire one. A restaurant in Tripoli that needed a bilingual menu. A book club in Beirut that needed a place to trade books. An accountant who wanted his Google Sheets to become a website.",
        "about_p2": "I work with AI the way a carpenter works with a nail gun — it's faster, it doesn't replace the judgment. Every project above was scoped, built, and shipped by one person, with AI in the loop. The ship times are real, because software doesn't have to take six months.",
        "experience_label": "Experience",
        "contact_label": "Contact",
        "contact_note": "I read everything and reply within a day, usually faster. If you're building something small and need it shipped before Friday, say so in the first line — I'll tell you honestly whether it's possible.",
        "smaller_work": "Smaller things: a Chrome extension that formats citations (1.2k weekly users), a Shopify webhook relay, a font-pairing tool that lives in a Figma plugin. All under a week each.",
        "footer_copy": "© 2025 Mohamed Belali",
        "footer_updated": "Made in Tripoli · Last updated October 2025",
        "copy_email": "Copy email",
        "copied": "Email copied to clipboard.",
        "404_title": "Page not found.",
        "404_desc": "The link you followed may be broken, or the page may have been removed.",
        "404_cta": "Back to home",
        "read_case_study": "Read case study",
        "back_to_work": "← Back to work",
        "problem": "The Problem",
        "process": "The Process",
        "solution": "The Solution",
        "result": "The Result",
    },
    "ar": {
        "kicker": "باني مستقل · طرابلس، لبنان",
        "hero_title": "أبني برمجيات في أيام. الذكاء الاصطناعي هو الوسيلة — مش الهدف.",
        "hero_lede": "محمد بيلالي. آخذ الأفكار من ملاحظة إلى منتج شغّال، غالباً قبل أن يُكتب مستند النطاق. أركز على إطلاق حلول حقيقية بسرعة، مع الحفاظ على العملية بسيطة.",
        "cta_work": "أعمال مختارة",
        "nav_work": "أعمالي",
        "nav_about": "نبذة",
        "nav_contact": "تواصل",
        "work_title": "أعمال مختارة",
        "work_intro": "ثلاثة مشاريع، أُطلقت بين 2023 و2024. كل واحد منها حُدّد نطاقه وبُني وأُدير بواسطة شخص واحد. مدد الإطلاق مذكورة لأنها الهدف — وليست استعراضاً.",
        "about_label": "نبذة",
        "about_p1": "أبني برمجيات منذ نحو أربع سنوات، معظمها لشركات صغيرة في بلاد الشام لا تملك فريقاً تقنياً ولا تنوي توظيف أحد. مطعم في طرابلس احتاج قائمة ثنائية اللغة. نادي قراءة في بيروت احتاج مكاناً لتبادل الكتب. محاسب أراد أن تتحوّل جداول Google إلى موقع.",
        "about_p2": "أعمل مع الذكاء الاصطناعي كما يعمل النجّار مع مسدّس المسامير — أسرع، لكنه لا يعوّض الحكم. كل مشروع أعلاه حُدّد نطاقه وبُني وأُطلق بواسطة شخص واحد، والذكاء الاصطناعي في الحلقة. مدد الإطلاق حقيقية، فالبرمجيات لا تحتاج أن تأخذ ستة أشهر.",
        "experience_label": "المسيرة",
        "contact_label": "للتواصل",
        "contact_note": "أقرأ كل شيء وأرد في غضون يوم، وغالباً أسرع. إذا كنت تبني شيئاً صغيراً وتحتاجه جاهزاً قبل الجمعة، فاذكر ذلك في السطر الأول — سأخبرك بصدق إن كان ذلك ممكناً أم لا.",
        "smaller_work": "أشياء أصغر: إضافة Chrome لتنسيق الاستشهادات (1.2 ألف مستخدم أسبوعياً)، وجسر webhooks لـ Shopify، وأداة لاقتران الخطوط تعمل كإضافة Figma. كل واحدة منها في أقل من أسبوع.",
        "footer_copy": "© 2025 محمد بيلالي",
        "footer_updated": "صُنع في طرابلس · آخر تحديث أكتوبر 2025",
        "copy_email": "نسخ البريد",
        "copied": "تم نسخ البريد الإلكتروني.",
        "404_title": "الصفحة غير موجودة.",
        "404_desc": "الرابط الذي تبعته قد يكون مكسوراً، أو ربما تم حذف الصفحة.",
        "404_cta": "العودة للرئيسية",
        "read_case_study": "اقرأ دراسة الحالة",
        "back_to_work": "← العودة للأعمال",
        "problem": "المشكلة",
        "process": "العملية",
        "solution": "الحل",
        "result": "النتيجة",
    },
}

PROJECTS = {
    "en": [
        {
            "slug": "deeb",
            "name": "Deeb — bilingual menu builder",
            "description": "A restaurant in Tripoli was reprinting menus every two weeks. I built a Flask app that turns a Google Sheet into a printable, scannable bilingual menu.",
            "year": 2024,
            "tech": "Flask · SQLite · WeasyPrint",
            "ship": "Shipped in 5 days · 12 restaurants using it",
        },
        {
            "slug": "masa",
            "name": "Masa — a book exchange for a reading group",
            "description": "A 40-person book club was running on three WhatsApp groups and a shared note. I built them an offline-first PWA.",
            "year": 2024,
            "tech": "Flask · SQLite · Service Worker",
            "ship": "Two weekends · 210 members, ~1,400 books exchanged",
        },
        {
            "slug": "sheet-to-site",
            "name": "Sheet-to-Site — a spreadsheet into a landing page",
            "description": "A tool I built for myself and then opened up. Paste a Google Sheet URL, pick a template, get a static site. No login. No dashboard.",
            "year": 2023,
            "tech": "Flask · Google Sheets API · PythonAnywhere",
            "ship": "Built in 3 days · ~3,000 sites generated",
        },
    ],
    "ar": [
        {
            "slug": "deeb",
            "name": "ديب — منشئ قوائم ثنائي اللغة",
            "description": "مطعم في طرابلس كان يعيد طباعة قوائمه كل أسبوعين. بنيت تطبيق Flask يحوّل جدول Google إلى قائمة ثنائية اللغة قابلة للطباعة.",
            "year": 2024,
            "tech": "Flask · SQLite · WeasyPrint",
            "ship": "أُطلق في 5 أيام · 12 مطعماً يستخدمه",
        },
        {
            "slug": "masa",
            "name": "ماسة — تبادل كتب لمجموعة قراءة",
            "description": "نادي كتاب من 40 شخصاً كان يعمل عبر ثلاث مجموعات WhatsApp وملاحظة مشتركة. بنيت لهم تطبيق ويب تقدّمي يعمل دون اتصال.",
            "year": 2024,
            "tech": "Flask · SQLite · Service Worker",
            "ship": "عطلتان أسبوعيتان · 210 أعضاء، ~1,400 كتاب تبادلوا",
        },
        {
            "slug": "sheet-to-site",
            "name": "Sheet-to-Site — من جدول بيانات إلى صفحة هبوط",
            "description": "أداة بنيتها لنفسي ثم أتحتها للعموم. الصق رابط Google Sheet، اختر قالباً، احصل على موقع ثابت. بلا تسجيل.",
            "year": 2023,
            "tech": "Flask · Google Sheets API · PythonAnywhere",
            "ship": "بُنيت في 3 أيام · ~3,000 موقع أُنشئ",
        },
    ],
}

CASE_STUDIES = {
    "en": {
        "deeb": {
            "title": "Deeb — bilingual menu builder",
            "meta": "2024 · Flask, SQLite, WeasyPrint",
            "problem": "The restaurant was printing 300 menus every two weeks. Every price change meant calling a designer, waiting three days, and paying for a full reprint. The waste was obvious, but the workflow was stuck.",
            "process": "I spent one afternoon with the owner, watching how she updated the menu. It was a Google Sheet. I realised the entire problem was a formatting issue — she already had the data, she just didn't have a way to make it look like a menu.",
            "solution": "I built a Flask app that reads the Google Sheet, renders it into a print-ready A4 PDF (using WeasyPrint), and handles RTL/LTR text mixing automatically. No login required. She edits the sheet, clicks a button, and prints.",
            "result": "The restaurant went from a 3-day turnaround to 30 seconds. They've stopped reprinting 300 menus at a time and only print what they need. 11 other restaurants in the area started using it."
        },
        "masa": {
            "title": "Masa — a book exchange for a reading group",
            "meta": "2024 · Flask, SQLite, Service Worker",
            "problem": "A 40-person book club was drowning in WhatsApp messages. Someone would post a book, it would get buried in 200 messages, and no one would find it. They needed a catalogue, not a chat.",
            "process": "I mapped the flow: a member lists a book, another member claims it, they meet, they swap. The entire system had to work on 3G because half the members were in areas with spotty coverage.",
            "solution": "I built an offline-first PWA. It caches the catalogue locally (Service Worker + IndexedDB). When a user opens the app, they see the latest list instantly, even with no connection. New listings sync when they get back online.",
            "result": "Over 1,400 books have been exchanged. The WhatsApp group is still there, but it's for chatting now, not logistics. The app handles 210 active members."
        },
        "sheet-to-site": {
            "title": "Sheet-to-Site — a spreadsheet into a landing page",
            "meta": "2023 · Flask, Google Sheets API",
            "problem": "I kept getting asked to build simple landing pages for people who already had their content in a spreadsheet. They didn't want a CMS, they didn't want a dashboard. They just wanted a URL.",
            "process": "I built a tool for myself first. Paste a Google Sheet URL, pick a template, get a static HTML site. I used it for three clients, then realised other people might want it.",
            "solution": "I opened it up. No login, no database. The site generates on the fly, reads the sheet, and spits out a clean page. Nothing is stored on my end.",
            "result": "Around 3,000 sites have been generated. I don't track users (no analytics), so I only know the number from the server logs. It still runs on the free tier."
        }
    },
    "ar": {
        "deeb": {
            "title": "ديب — منشئ قوائم ثنائي اللغة",
            "meta": "2024 · Flask, SQLite, WeasyPrint",
            "problem": "المطعم كان يطبع 300 قائمة كل أسبوعين. أي تغيير في السعر يعني الاتصال بمصمم، الانتظار ثلاثة أيام، والدفع لإعادة طباعة كاملة. الهدر كان واضحاً، لكن سير العمل كان متجمداً.",
            "process": "أمضيت فترة بعد الظهر مع صاحبة المطعم، أراقب كيف تحدّث القائمة. كانت جدول Google. أدركت أن المشكلة كلها كانت في التنسيق — هي بالفعل تملك البيانات، لكنها لم تملك طريقة لجعلها تبدو كقائمة.",
            "solution": "بنيت تطبيق Flask يقرأ جدول Google، ويحوّله إلى PDF جاهز للطباعة (باستخدام WeasyPrint)، ويتعامل مع خلط النصوص RTL/LTR تلقائياً. لا يتطلب تسجيل دخول. تعدّل الجدول، تضغط زراً، وتطبع.",
            "result": "انتقل المطعم من دورة إنتاج استغرقت 3 أيام إلى 30 ثانية. توقفوا عن طباعة 300 قائمة دفعة واحدة ويطبعون فقط ما يحتاجونه. 11 مطعماً آخر في المنطقة بدأوا يستخدمونه."
        },
        "masa": {
            "title": "ماسة — تبادل كتب لمجموعة قراءة",
            "meta": "2024 · Flask, SQLite, Service Worker",
            "problem": "نادي كتاب من 40 شخصاً كان يغرق في رسائل WhatsApp. ينشر أحدهم كتاباً، فيدفن وسط 200 رسالة، ولا يجده أحد. احتاجوا كتالوجاً، لا محادثة.",
            "process": "رسمت مسار العمل: يدرج عضو كتاباً، يطالب به عضو آخر، يلتقيان، يتبادلان. النظام بأكمله كان يجب أن يعمل على 3G لأن نصف الأعضاء في مناطق تغطيتها ضعيفة.",
            "solution": "بنيت تطبيق ويب تقدّمي يعمل دون اتصال. يخزّن الكتالوج محلياً (Service Worker + IndexedDB). عند فتح التطبيق، يرى المستخدم أحدث قائمة فوراً، حتى بدون اتصال. تتم مزامنة الإدراجات الجديدة عند العودة للاتصال.",
            "result": "تم تبادل أكثر من 1,400 كتاب. مجموعة WhatsApp لا تزال موجودة، لكنها للدردشة الآن، لا للوجستيات. التطبيق يدير 210 أعضاء نشطين."
        },
        "sheet-to-site": {
            "title": "Sheet-to-Site — من جدول بيانات إلى صفحة هبوط",
            "meta": "2023 · Flask, Google Sheets API",
            "problem": "ظللت أُطلب لبناء صفحات هبوط بسيطة لأشخاص لديهم محتواهم بالفعل في جدول بيانات. لم يريدوا نظام إدارة محتوى، لم يريدوا لوحة تحكم. أرادوا رابطاً فقط.",
            "process": "بنيت أداة لنفسي أولاً. الصق رابط Google Sheet، اختر قالباً، احصل على موقع HTML ثابت. استخدمتها لثلاثة عملاء، ثم أدركت أن الآخرين قد يريدونها.",
            "solution": "فتحتها للعموم. بلا تسجيل، بلا قاعدة بيانات. يُولّد الموقع في اللحظة، يقرأ الجدول، ويُخرج صفحة نظيفة. لا شيء يُخزَّن عندي.",
            "result": "تم توليد حوالي 3,000 موقع. لا أتتبع المستخدمين (بلا تحليلات)، لذا أعرف الرقم فقط من سجلات الخادم. لا يزال يعمل على الطبقة المجانية."
        }
    }
}

EXPERIENCE = {
    "en": [
        {"years": "2024 — now", "role": "Independent product builder", "detail": "Scoping, building, and maintaining software for small businesses in Lebanon and the wider MENA region."},
        {"years": "2022 — 2024", "role": "Backend engineer · Halab Studio", "detail": "Built client-facing sites and internal tools for a Beirut-based studio. Left as the only backend engineer on three concurrent projects."},
        {"years": "2020 — 2022", "role": "Learning in public", "detail": "First freelance work — three sites, one Shopify integration, one very long year of reading other people's code."},
    ],
    "ar": [
        {"years": "2024 — الآن", "role": "باني منتجات مستقل", "detail": "تحديد النطاق والبناء والصيانة لبرمجيات شركات صغيرة في لبنان ومنطقة الشرق الأوسط الأوسع."},
        {"years": "2022 — 2024", "role": "مهندس Backend · Halab Studio", "detail": "بنيت مواقع للعملاء وأدوات داخلية لاستوديو مقره بيروت. تركت العمل كالمهندس الوحيد للـ backend على ثلاثة مشاريع متزامنة."},
        {"years": "2020 — 2022", "role": "التعلّم على الملأ", "detail": "أول عمل حر — ثلاثة مواقع، وتكامل Shopify واحد، وسنة طويلة جداً من قراءة أكواد الآخرين."},
    ],
}

SUPPORTED = {"en", "ar"}
