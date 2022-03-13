-- Создание таблиц

DROP TABLE IF EXISTS menus;

CREATE TABLE menus (
    charCode text NOT NULL,
    location text NOT NULL,
    type text,
    goBack bool,
    goBackText text,
    PRIMARY KEY(charCode, location)
);


DROP TABLE IF EXISTS buttons;

CREATE TABLE buttons (
    menuCode varchar(255) NOT NULL,
    sort int NOT NULL,
    text text,
    icon text,
    detail text,
    link text,
    onClick text,
    PRIMARY KEY(menuCode, sort),
    FOREIGN KEY(menuCode) REFERENCES menus(charCode)
);

INSERT INTO menus(charCode, location, type, goBack, goBackText)
VALUES
    ("MAIN",                 "",                     "MAIN",         false,  NULL),
    ("MAPS",                 "maps",                "TWO_SIDES",    true,   "Назад"),
    ("SERVICES",             "services",            "TWO_SIDES",    true,   "Назад"),
    ("SERVICES_FINANCE",    "services/finance",     "TWO_SIDES",   true,   "Назад")
;

INSERT INTO buttons(menuCode, sort, text, icon, detail, link, onClick)
VALUES
    -- MAIN MENU BEGIN --
    (
        -- button to services BEGIN --
        "MAIN",
        0,
        "Справки, услуги",
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>',
        NULL,
        "/services",
        NULL
        -- button to services END --
    ),
    (
        -- button to news BEGIN --
        "MAIN",
        1,
        "Вагон новостей",
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
                    </svg>',
        NULL,
        "/news",
        NULL
        -- button to news END --
    ),
    (
        -- button to maps BEGIN --
        "MAIN",
        2,
        "Карта предприятия",
        '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z">
                    </path></svg>',
        NULL,
        "/maps",
        NULL
        -- button to maps END --
    ),
    -- MAIN MENU END --

    -- MAPS MENU BEGIN --
    (
        -- button to ruzkhimmash BEGIN --
        "MAPS",
        0,
        'АО "РУЗХИММАШ"',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>',
        NULL,
        "/maps/ruzkhimmash",
        NULL
        -- button to ruzkhimmash END --
    ),
    -- MAPS MENU END --

    -- SERVICES MENU BEGIN --
    (
        -- button to finance BEGIN --
        "SERVICES",
        0,
        "Доходы",
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>',
        'Справка 2-НДФЛ, Справка 182Н, Справка о заработной плате,
                Справка в УФССП, Справка в центр занятости',
        "/services/finance",
        NULL
        -- button to finance END --
    ),
    (
        -- button to payments BEGIN --
        "SERVICES",
        1,
        "Выплаты",
        '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>',
        'Справка о выплате единовременного пособия, 
                Справка о получении/неполучении пособия по уходу за ребенком, 
                Справка о выплате материальной помощи при рождении ребенка',
        -- TODO: ПОМЕНЯТЬ ССЫЛКУ --
        "/forms/service/1",
        NULL
        -- button to payments END --
    ),
    -- SERVICES MENU END --

    -- SERVICES_FINANCE MENU BEGIN --
    (
        -- button to form 2-НДФЛ BEGIN --
        "SERVICES_FINANCE",
        0,
        "Справка 2-НДФЛ",
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>',
        NULL,
        "/services/finance",
        NULL
        -- button to form 2-НДФЛ END --
    )
    -- SERVICES_FINANCE MENU END --

;