/**
 * KernelGuard Internationalization (i18n) Module
 * Supports: English, Türkçe, Deutsch, Français
 * Uses data-i18n attributes on HTML elements to swap text content.
 * Persists language choice in localStorage.
 */

const translations = {
    en: {
        // Navigation
        "nav.whatWeBuild": "What We Build",
        "nav.projects": "Projects",
        "nav.about": "About",
        "nav.contact": "Contact",
        "nav.search.placeholder": "Search all of KernelGuard",
        "nav.lang.header": "Select Language",
        "nav.help.title": "Help & Information",
        "nav.help.gettingStarted": "Getting Started",
        "nav.help.documentation": "Documentation",
        "nav.help.apiReference": "API Reference",
        "nav.help.securityPolicy": "Security Policy",
        "nav.help.companyBlock": "KernelGuard Inc.<br>Secure Systems Infrastructure<br>v2.1.0-beta",
        "nav.help.contactSupport": "Contact Support →",
        "nav.user.myProfile": "My Profile",
        "nav.user.myProjects": "My Projects",
        "nav.user.teamName": "KernelGuard Team",
        "nav.user.teamDesc": "A specialized 3-person development collective focused on systems engineering, rigorous cybersecurity, and scalable full-stack infrastructure.",

        // Hero
        "hero.tagline": "Kernel Guard builds secure systems, intelligent infrastructure, and scalable web platforms.<br><br>We focus on cybersecurity, systems engineering, and production-grade software designed for reliability, performance, and long-term maintainability.",
        "hero.cta": "See Our Work",

        // Services
        "services.title": "What We Build",
        "services.secure": "Secure systems and security-focused infrastructure.",
        "services.intelligent": "Intelligent platforms powered by AI and data-driven engineering.",
        "services.scalable": "Scalable backend and web applications.",
        "services.highPerf": "High-performance software with strong operational discipline.",

        // Core Areas
        "core.title": "Core Areas",
        "core.cybersecurity": "Cybersecurity Engineering",
        "core.ebpf": "eBPF and Runtime Security",
        "core.systems": "Systems Programming",
        "core.cloud": "Cloud and Infrastructure Engineering",
        "core.ai": "AI-Driven Systems",
        "core.web": "Scalable Web Platforms",

        // Flagship Projects
        "projects.title": "Flagship Projects",
        "projects.openSource": "Open Source Projects",
        "projects.closedSource": "Closed Source Projects (Demos)",
        "projects.aegis.title": "Aegis-BPF",
        "projects.aegis.desc": "A runtime security engine built with eBPF CO-RE and LSM-based enforcement, designed for synchronous kernel-level protection.",
        "projects.cathodex.title": "CathodeX",
        "projects.cathodex.desc": "High-performance userspace networking stack engineered in C, optimized for massive concurrency and determinism.",
        "projects.eduhub.title": "EduHub Campus",
        "projects.eduhub.desc": "A B2B enterprise room and resource reservation system with secure tenant-based isolation and audit trails.",
        "projects.refatelier.title": "Ref Atelier",
        "projects.refatelier.desc": "A high-performance luxury e-commerce frontend architecture ensuring fast load times and seamless localization.",

        // About / Engineering Principles
        "about.principles.title": "Engineering Principles",
        "about.principles.weValue": "We value:",
        "about.principles.security": "Security by design",
        "about.principles.performance": "Measured performance",
        "about.principles.contracts": "Clear operational contracts",
        "about.principles.production": "Production readiness",
        "about.principles.evidence": "Evidence over claims",
        "about.mission.title": "Mission",
        "about.mission.text": "Kernel Guard exists to build software that is not only functional, but secure, resilient, and engineered to hold up under real-world conditions.",

        // Footer
        "footer.cta.title": "Ready to build something serious?",
        "footer.cta.desc": "For collaborations, partnerships, or technical discussions, feel free to reach out.",
        "footer.cta.btn": "Contact Us",
        "footer.copyright": "KernelGuard Inc. &copy; 2026",

        // Project Detail Pages
        "project.back": "Back to Directory",
        "project.techOverview": "Technical Overview",
        "project.valueProp": "Value Proposition",
        "project.viewSource": "View Source Code",
        "project.viewDemo": "View Demo Portal",
        "project.viewStorefront": "View Storefront",

        // Contact
        "contact.title": 'Ready to build something serious?',
        "contact.desc": 'For collaborations, partnerships, or technical discussions — reach out directly. We respond within 24 hours.',
        "contact.name": 'Name',
        "contact.name.placeholder": 'Your full name',
        "contact.org": 'Organization',
        "contact.org.placeholder": 'Company or institution',
        "contact.email": 'Work Email',
        "contact.email.placeholder": 'you@company.com',
        "contact.email.error": 'Please enter a valid email address.',
        "contact.message": 'Message',
        "contact.message.placeholder": 'Tell us about your project or inquiry...',
        "contact.send": 'Send Message',
        "contact.sending": 'Sending...',
        "contact.toast": 'Message sent successfully. We\'ll be in touch soon.',
        "contact.team.title": 'Connect with the Team',
        "contact.team.desc": 'Our founding engineers are available on LinkedIn for professional inquiries and collaboration.',
        "contact.team.role1": 'Full-Stack Developer',
        "contact.team.role2": 'Software Developer',
        "contact.team.role3": 'Design Engineer',
    },

    tr: {
        // Navigasyon
        "nav.whatWeBuild": "Ne İnşa Ediyoruz",
        "nav.projects": "Projeler",
        "nav.about": "Hakkımızda",
        "nav.contact": "İletişim",
        "nav.search.placeholder": "KernelGuard genelinde arayın",
        "nav.lang.header": "Dil Seçin",
        "nav.help.title": "Yardım & Bilgi",
        "nav.help.gettingStarted": "Başlarken",
        "nav.help.documentation": "Dokümantasyon",
        "nav.help.apiReference": "API Referansı",
        "nav.help.securityPolicy": "Güvenlik Politikası",
        "nav.help.companyBlock": "KernelGuard Inc.<br>Güvenli Sistem Altyapısı<br>v2.1.0-beta",
        "nav.help.contactSupport": "Destek ile İletişim →",
        "nav.user.myProfile": "Profilim",
        "nav.user.myProjects": "Projelerim",
        "nav.user.teamName": "KernelGuard Ekibi",
        "nav.user.teamDesc": "Sistem mühendisliği, siber güvenlik ve ölçeklenebilir tam yığın altyapıya odaklanan 3 kişilik uzman geliştirici kolektifi.",

        // Hero
        "hero.tagline": "Kernel Guard güvenli sistemler, akıllı altyapılar ve ölçeklenebilir web platformları inşa eder.<br><br>Siber güvenlik, sistem mühendisliği ve güvenilirlik, performans ve uzun vadeli sürdürülebilirlik için tasarlanmış üretim kalitesinde yazılıma odaklanıyoruz.",
        "hero.cta": "Çalışmalarımızı Görün",

        // Hizmetler
        "services.title": "Ne İnşa Ediyoruz",
        "services.secure": "Güvenli sistemler ve güvenlik odaklı altyapı.",
        "services.intelligent": "Yapay zeka ve veri odaklı mühendislik ile güçlendirilmiş akıllı platformlar.",
        "services.scalable": "Ölçeklenebilir backend ve web uygulamaları.",
        "services.highPerf": "Güçlü operasyonel disiplinle yüksek performanslı yazılım.",

        // Temel Alanlar
        "core.title": "Temel Alanlar",
        "core.cybersecurity": "Siber Güvenlik Mühendisliği",
        "core.ebpf": "eBPF ve Çalışma Zamanı Güvenliği",
        "core.systems": "Sistem Programlama",
        "core.cloud": "Bulut ve Altyapı Mühendisliği",
        "core.ai": "Yapay Zeka Tabanlı Sistemler",
        "core.web": "Ölçeklenebilir Web Platformları",

        // Amiral Gemisi Projeleri
        "projects.title": "Amiral Gemisi Projeleri",
        "projects.openSource": "Açık Kaynak Projeler",
        "projects.closedSource": "Kapalı Kaynak Projeler (Demolar)",
        "projects.aegis.title": "Aegis-BPF",
        "projects.aegis.desc": "eBPF CO-RE ve LSM tabanlı uygulama ile inşa edilmiş, eşzamanlı çekirdek düzeyinde koruma için tasarlanmış bir çalışma zamanı güvenlik motoru.",
        "projects.cathodex.title": "CathodeX",
        "projects.cathodex.desc": "C ile geliştirilen, yoğun eşzamanlılık ve determinizm için optimize edilmiş yüksek performanslı kullanıcı alanı ağ yığını.",
        "projects.eduhub.title": "EduHub Kampüs",
        "projects.eduhub.desc": "Güvenli kiracı tabanlı izolasyon ve denetim izleriyle B2B kurumsal oda ve kaynak rezervasyon sistemi.",
        "projects.refatelier.title": "Ref Atelier",
        "projects.refatelier.desc": "Hızlı yükleme süreleri ve sorunsuz yerelleştirme sağlayan yüksek performanslı lüks e-ticaret ön yüz mimarisi.",

        // Hakkında / Mühendislik İlkeleri
        "about.principles.title": "Mühendislik İlkeleri",
        "about.principles.weValue": "Değer verdiklerimiz:",
        "about.principles.security": "Tasarımdan güvenlik",
        "about.principles.performance": "Ölçülü performans",
        "about.principles.contracts": "Net operasyonel sözleşmeler",
        "about.principles.production": "Üretime hazırlık",
        "about.principles.evidence": "İddialara karşı kanıt",
        "about.mission.title": "Misyon",
        "about.mission.text": "Kernel Guard yalnızca işlevsel değil, aynı zamanda güvenli, dayanıklı ve gerçek dünya koşullarında ayakta kalmak için mühendislikle tasarlanmış yazılımlar inşa etmek için vardır.",

        // Altbilgi
        "footer.cta.title": "Ciddi bir şey inşa etmeye hazır mısınız?",
        "footer.cta.desc": "İş birlikleri, ortaklıklar veya teknik tartışmalar için bizimle iletişime geçin.",
        "footer.cta.btn": "İletişim",
        "footer.copyright": "KernelGuard Inc. &copy; 2026",

        // Proje Detay Sayfaları
        "project.back": "Dizine Dön",
        "project.techOverview": "Teknik Genel Bakış",
        "project.valueProp": "Değer Önerisi",
        "project.viewSource": "Kaynak Kodunu Görüntüle",
        "project.viewDemo": "Demo Portalını Görüntüle",
        "project.viewStorefront": "Mağazayı Görüntüle",

        // İletişim
        "contact.title": 'Ciddi bir şey inşa etmeye hazır mısınız?',
        "contact.desc": 'İş birlikleri, ortaklıklar veya teknik tartışmalar için doğrudan bize ulaşın. 24 saat içinde yanıt veriyoruz.',
        "contact.name": 'İsim',
        "contact.name.placeholder": 'Tam adınız',
        "contact.org": 'Kuruluş',
        "contact.org.placeholder": 'Şirket veya kurum',
        "contact.email": 'İş E-postası',
        "contact.email.placeholder": 'siz@sirket.com',
        "contact.email.error": 'Lütfen geçerli bir e-posta adresi girin.',
        "contact.message": 'Mesaj',
        "contact.message.placeholder": 'Projeniz veya sorunuz hakkında bilgi verin...',
        "contact.send": 'Mesaj Gönder',
        "contact.sending": 'Gönderiliyor...',
        "contact.toast": 'Mesaj başarıyla gönderildi. En kısa sürede dönüş yapacağız.',
        "contact.team.title": 'Ekible İletişim Kurun',
        "contact.team.desc": 'Kurucu mühendislerimiz profesyonel sorular ve iş birliği için LinkedIn\'de mevcuttur.',
        "contact.team.role1": 'Full-Stack Geliştirici',
        "contact.team.role2": 'Yazılım Geliştirici',
        "contact.team.role3": 'Tasarım Mühendisi',
    },

    de: {
        // Navigation
        "nav.whatWeBuild": "Was Wir Bauen",
        "nav.projects": "Projekte",
        "nav.about": "Über Uns",
        "nav.contact": "Kontakt",
        "nav.search.placeholder": "Alles in KernelGuard durchsuchen",
        "nav.lang.header": "Sprache wählen",
        "nav.help.title": "Hilfe & Informationen",
        "nav.help.gettingStarted": "Erste Schritte",
        "nav.help.documentation": "Dokumentation",
        "nav.help.apiReference": "API-Referenz",
        "nav.help.securityPolicy": "Sicherheitsrichtlinie",
        "nav.help.companyBlock": "KernelGuard Inc.<br>Sichere Systeminfrastruktur<br>v2.1.0-beta",
        "nav.help.contactSupport": "Support kontaktieren →",
        "nav.user.myProfile": "Mein Profil",
        "nav.user.myProjects": "Meine Projekte",
        "nav.user.teamName": "KernelGuard Team",
        "nav.user.teamDesc": "Ein spezialisiertes 3-Personen-Entwicklungskollektiv mit Fokus auf Systemtechnik, Cybersicherheit und skalierbare Full-Stack-Infrastruktur.",

        // Hero
        "hero.tagline": "Kernel Guard entwickelt sichere Systeme, intelligente Infrastruktur und skalierbare Webplattformen.<br><br>Wir konzentrieren uns auf Cybersicherheit, Systemtechnik und produktionsreife Software, die auf Zuverlässigkeit, Leistung und langfristige Wartbarkeit ausgelegt ist.",
        "hero.cta": "Unsere Arbeit ansehen",

        // Dienstleistungen
        "services.title": "Was Wir Bauen",
        "services.secure": "Sichere Systeme und sicherheitsorientierte Infrastruktur.",
        "services.intelligent": "Intelligente Plattformen angetrieben durch KI und datengesteuerte Entwicklung.",
        "services.scalable": "Skalierbare Backend- und Webanwendungen.",
        "services.highPerf": "Hochleistungssoftware mit starker operationeller Disziplin.",

        // Kernbereiche
        "core.title": "Kernbereiche",
        "core.cybersecurity": "Cybersicherheitstechnik",
        "core.ebpf": "eBPF und Laufzeitsicherheit",
        "core.systems": "Systemprogrammierung",
        "core.cloud": "Cloud- und Infrastrukturtechnik",
        "core.ai": "KI-gesteuerte Systeme",
        "core.web": "Skalierbare Webplattformen",

        // Flaggschiff-Projekte
        "projects.title": "Flaggschiff-Projekte",
        "projects.openSource": "Open-Source-Projekte",
        "projects.closedSource": "Geschlossene Projekte (Demos)",
        "projects.aegis.title": "Aegis-BPF",
        "projects.aegis.desc": "Eine Laufzeit-Sicherheitsengine, gebaut mit eBPF CO-RE und LSM-basierter Durchsetzung für synchronen Schutz auf Kernel-Ebene.",
        "projects.cathodex.title": "CathodeX",
        "projects.cathodex.desc": "Hochleistungs-Userspace-Netzwerkstack in C entwickelt, optimiert für massive Parallelität und Determinismus.",
        "projects.eduhub.title": "EduHub Campus",
        "projects.eduhub.desc": "Ein B2B-Unternehmens-Reservierungssystem für Räume und Ressourcen mit sicherer Mandantentrennung und Audit-Protokollen.",
        "projects.refatelier.title": "Ref Atelier",
        "projects.refatelier.desc": "Hochleistungs-Frontend-Architektur für Luxus-E-Commerce mit schnellen Ladezeiten und nahtloser Lokalisierung.",

        // Über / Ingenieurprinzipien
        "about.principles.title": "Ingenieurprinzipien",
        "about.principles.weValue": "Unsere Werte:",
        "about.principles.security": "Sicherheit durch Design",
        "about.principles.performance": "Gemessene Leistung",
        "about.principles.contracts": "Klare Betriebsverträge",
        "about.principles.production": "Produktionsbereitschaft",
        "about.principles.evidence": "Beweise statt Behauptungen",
        "about.mission.title": "Mission",
        "about.mission.text": "Kernel Guard existiert, um Software zu entwickeln, die nicht nur funktional, sondern sicher, belastbar und für reale Bedingungen konstruiert ist.",

        // Fußzeile
        "footer.cta.title": "Bereit, etwas Ernsthaftes zu bauen?",
        "footer.cta.desc": "Für Zusammenarbeit, Partnerschaften oder technische Diskussionen kontaktieren Sie uns.",
        "footer.cta.btn": "Kontaktieren",
        "footer.copyright": "KernelGuard Inc. &copy; 2026",

        // Projektdetailseiten
        "project.back": "Zurück zum Verzeichnis",
        "project.techOverview": "Technische Übersicht",
        "project.valueProp": "Wertversprechen",
        "project.viewSource": "Quellcode anzeigen",
        "project.viewDemo": "Demo-Portal anzeigen",
        "project.viewStorefront": "Storefront anzeigen",

        // Kontakt
        "contact.title": 'Bereit, etwas Ernsthaftes zu bauen?',
        "contact.desc": 'Für Zusammenarbeit, Partnerschaften oder technische Diskussionen — kontaktieren Sie uns direkt. Wir antworten innerhalb von 24 Stunden.',
        "contact.name": 'Name',
        "contact.name.placeholder": 'Ihr vollständiger Name',
        "contact.org": 'Organisation',
        "contact.org.placeholder": 'Unternehmen oder Institution',
        "contact.email": 'Geschäfts-E-Mail',
        "contact.email.placeholder": 'sie@unternehmen.com',
        "contact.email.error": 'Bitte geben Sie eine gültige E-Mail-Adresse ein.',
        "contact.message": 'Nachricht',
        "contact.message.placeholder": 'Erzählen Sie uns von Ihrem Projekt oder Ihrer Anfrage...',
        "contact.send": 'Nachricht senden',
        "contact.sending": 'Wird gesendet...',
        "contact.toast": 'Nachricht erfolgreich gesendet. Wir melden uns in Kürze.',
        "contact.team.title": 'Verbinden Sie sich mit dem Team',
        "contact.team.desc": 'Unsere Gründungsingenieure sind auf LinkedIn für professionelle Anfragen und Zusammenarbeit verfügbar.',
        "contact.team.role1": 'Full-Stack-Entwickler',
        "contact.team.role2": 'Softwareentwickler',
        "contact.team.role3": 'Designingenieur',
    },

    fr: {
        // Navigation
        "nav.whatWeBuild": "Ce Que Nous Construisons",
        "nav.projects": "Projets",
        "nav.about": "À Propos",
        "nav.contact": "Contact",
        "nav.search.placeholder": "Rechercher dans KernelGuard",
        "nav.lang.header": "Choisir la langue",
        "nav.help.title": "Aide & Informations",
        "nav.help.gettingStarted": "Premiers Pas",
        "nav.help.documentation": "Documentation",
        "nav.help.apiReference": "Référence API",
        "nav.help.securityPolicy": "Politique de Sécurité",
        "nav.help.companyBlock": "KernelGuard Inc.<br>Infrastructure Systèmes Sécurisés<br>v2.1.0-beta",
        "nav.help.contactSupport": "Contacter le Support →",
        "nav.user.myProfile": "Mon Profil",
        "nav.user.myProjects": "Mes Projets",
        "nav.user.teamName": "Équipe KernelGuard",
        "nav.user.teamDesc": "Un collectif spécialisé de 3 développeurs axé sur l'ingénierie des systèmes, la cybersécurité rigoureuse et l'infrastructure full-stack évolutive.",

        // Hero
        "hero.tagline": "Kernel Guard construit des systèmes sécurisés, des infrastructures intelligentes et des plateformes web évolutives.<br><br>Nous nous concentrons sur la cybersécurité, l'ingénierie des systèmes et les logiciels de production conçus pour la fiabilité, la performance et la maintenabilité à long terme.",
        "hero.cta": "Voir Nos Réalisations",

        // Services
        "services.title": "Ce Que Nous Construisons",
        "services.secure": "Systèmes sécurisés et infrastructure axée sur la sécurité.",
        "services.intelligent": "Plateformes intelligentes alimentées par l'IA et l'ingénierie des données.",
        "services.scalable": "Applications backend et web évolutives.",
        "services.highPerf": "Logiciels haute performance avec une forte discipline opérationnelle.",

        // Domaines clés
        "core.title": "Domaines Clés",
        "core.cybersecurity": "Ingénierie en Cybersécurité",
        "core.ebpf": "eBPF et Sécurité d'Exécution",
        "core.systems": "Programmation Systèmes",
        "core.cloud": "Ingénierie Cloud et Infrastructure",
        "core.ai": "Systèmes Pilotés par l'IA",
        "core.web": "Plateformes Web Évolutives",

        // Projets phares
        "projects.title": "Projets Phares",
        "projects.openSource": "Projets Open Source",
        "projects.closedSource": "Projets Privés (Démos)",
        "projects.aegis.title": "Aegis-BPF",
        "projects.aegis.desc": "Un moteur de sécurité d'exécution construit avec eBPF CO-RE et l'application basée sur LSM, conçu pour la protection synchrone au niveau du noyau.",
        "projects.cathodex.title": "CathodeX",
        "projects.cathodex.desc": "Pile réseau hautes performances en espace utilisateur développée en C, optimisée pour une concurrence massive et le déterminisme.",
        "projects.eduhub.title": "EduHub Campus",
        "projects.eduhub.desc": "Un système B2B de réservation de salles et de ressources avec isolation sécurisée des locataires et pistes d'audit.",
        "projects.refatelier.title": "Ref Atelier",
        "projects.refatelier.desc": "Architecture frontend e-commerce de luxe haute performance assurant des temps de chargement rapides et une localisation fluide.",

        // À propos / Principes d'ingénierie
        "about.principles.title": "Principes d'Ingénierie",
        "about.principles.weValue": "Nos valeurs :",
        "about.principles.security": "Sécurité dès la conception",
        "about.principles.performance": "Performance mesurée",
        "about.principles.contracts": "Contrats opérationnels clairs",
        "about.principles.production": "Prêt pour la production",
        "about.principles.evidence": "Preuves plutôt que déclarations",
        "about.mission.title": "Mission",
        "about.mission.text": "Kernel Guard existe pour construire des logiciels qui sont non seulement fonctionnels, mais sécurisés, résilients et conçus pour résister aux conditions réelles.",

        // Pied de page
        "footer.cta.title": "Prêt à construire quelque chose de sérieux ?",
        "footer.cta.desc": "Pour des collaborations, des partenariats ou des discussions techniques, n'hésitez pas à nous contacter.",
        "footer.cta.btn": "Contactez-nous",
        "footer.copyright": "KernelGuard Inc. &copy; 2026",

        // Pages détails projet
        "project.back": "Retour au Répertoire",
        "project.techOverview": "Aperçu Technique",
        "project.valueProp": "Proposition de Valeur",
        "project.viewSource": "Voir le Code Source",
        "project.viewDemo": "Voir le Portail Démo",
        "project.viewStorefront": "Voir la Boutique",

        // Contact
        "contact.title": 'Prêt à construire quelque chose de sérieux ?',
        "contact.desc": 'Pour des collaborations, des partenariats ou des discussions techniques — contactez-nous directement. Nous répondons sous 24 heures.',
        "contact.name": 'Nom',
        "contact.name.placeholder": 'Votre nom complet',
        "contact.org": 'Organisation',
        "contact.org.placeholder": 'Entreprise ou institution',
        "contact.email": 'E-mail professionnel',
        "contact.email.placeholder": 'vous@entreprise.com',
        "contact.email.error": 'Veuillez entrer une adresse e-mail valide.',
        "contact.message": 'Message',
        "contact.message.placeholder": 'Parlez-nous de votre projet ou de votre demande...',
        "contact.send": 'Envoyer le message',
        "contact.sending": 'Envoi en cours...',
        "contact.toast": 'Message envoyé avec succès. Nous vous répondrons bientôt.',
        "contact.team.title": 'Connectez-vous avec l\'Équipe',
        "contact.team.desc": 'Nos ingénieurs fondateurs sont disponibles sur LinkedIn pour les demandes professionnelles et la collaboration.',
        "contact.team.role1": 'Développeur Full-Stack',
        "contact.team.role2": 'Développeur Logiciel',
        "contact.team.role3": 'Ingénieur Design',
    }
};

/**
 * Apply translations to all elements with data-i18n attribute
 */
function applyTranslation(lang) {
    const dict = translations[lang];
    if (!dict) return;

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });

    // Handle placeholder attributes separately
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (dict[key]) {
            el.setAttribute('placeholder', dict[key]);
        }
    });

    // Save preference
    localStorage.setItem('kg-lang', lang);

    // Update active state in lang rows
    document.querySelectorAll('.lang-row').forEach(row => {
        row.classList.toggle('active', row.getAttribute('data-lang') === lang);
    });

    // Globe indicator dot
    const btnLang = document.getElementById('btn-lang');
    if (btnLang) {
        btnLang.classList.toggle('active', lang !== 'en');
    }
}

/**
 * Initialize i18n on page load
 */
function initI18n() {
    const savedLang = localStorage.getItem('kg-lang') || 'en';
    if (savedLang !== 'en') {
        applyTranslation(savedLang);
    }
}

// Auto-initialize
document.addEventListener('DOMContentLoaded', initI18n);
