/*
----------------------------------------------------------------------
International Organization for Standardization (ISO) Database Schema
----------------------------------------------------------------------
This script is a customized database for geographic information for
the global standards for trusted goods and services. ISO is an
independent, non-governmental international organization. It brings
global experts together to agree on the best ways of doing things.

Procured by Jason Monroe (jason@jasonmonroe.com)

Note: Storing latitude and longitude coordinates for the Haversine
Formula.

@link https://www.iso.org/home.html
@link https://www.iso.org/obp/ui/#search
@link https://www.iso.org/obp/ui/#iso:pub:PUB500001:en
@link https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
@link https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
@link https://mkyong.com/java8/java-display-all-zoneid-and-its-utc-offset/
@link https://www.timeanddate.com/time/zones/
*/

CREATE DATABASE IF NOT EXISTS iso
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE iso;

CREATE TABLE location (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    coordinates POINT NOT NULL SRID 4326, -- used for Geographic Information System
    SPATIAL INDEX(coordinates),  -- Enables efficient spatial queries
    latitude DECIMAL(11, 8), -- used for Haversine Formula (North to South)
    longitude DECIMAL(11, 8), -- used for Haversine Formula (East to West)
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id)
);

CREATE TABLE timezone (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    standard_time_name VARCHAR(64) NOT NULL, -- i.e: Central Standard Time
    name VARCHAR(32) NOT NULL, -- i.e: America/Chicago
    offset VARCHAR(16), -- i.e: UTC+12:00
    group_offset BOOLEAN DEFAULT FALSE, -- used to group timezones by offset to prevent displaying all timezones
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id)
    );

INSERT INTO timezone (standard_time_name, name, offset) VALUES
-- International Line (Start) East to West
-- Earliest timezone
('Line Islands Time', 'Pacific/Kiritimati', 'UTC+14:00'),
('Tokelau Time', 'Pacific/Fakaofo', 'UTC+13:00'),
('Phoenix Islands Time', 'Pacific/Enderbury', 'UTC+13:00'),
('Samoa Time', 'Pacific/Apia', 'UTC+13:00'),
('Tonga Time', 'Pacific/Tongatapu', 'UTC+13:00'),
('Chatham Standard Time', 'Pacific/Chatham', 'UTC+12:45'),
('Marshall Islands Time', 'Pacific/Kwajalein', 'UTC+12:00'),
('New Zealand Standard Time', 'Antarctica/McMurdo', 'UTC+12:00'),
('Wallis and Futuna Time', 'Pacific/Wallis', 'UTC+12:00'),
('Fiji Time', 'Pacific/Fiji', 'UTC+12:00'),
('Tuvalu Time', 'Pacific/Funafuti', 'UTC+12:00'),
('Nauru Time', 'Pacific/Nauru', 'UTC+12:00'),
('Marshall Islands Time', 'Kwajalein', 'UTC+12:00'),
('New Zealand Standard Time', 'NZ', 'UTC+12:00'),
('Wake Island Time', 'Pacific/Wake', 'UTC+12:00'),
('Antarctica Time', 'Antarctica/South_Pole', 'UTC+12:00'),
('Gilbert Islands Time', 'Pacific/Tarawa', 'UTC+12:00'),
('New Zealand Standard Time', 'Pacific/Auckland', 'UTC+12:00'),
('Kamchatka Time', 'Asia/Kamchatka', 'UTC+12:00'),
('Anadyr Time', 'Asia/Anadyr', 'UTC+12:00'),
('Marshall Islands Time', 'Pacific/Majuro', 'UTC+12:00'),
('Chuuk Time', 'Pacific/Ponape', 'UTC+11:00'),
('Solomon Islands Time', 'Pacific/Bougainville', 'UTC+11:00'),
('Macquarie Island Time', 'Antarctica/Macquarie', 'UTC+11:00'),
('Chuuk Time', 'Pacific/Pohnpei', 'UTC+11:00'),
('Vanuatu Time', 'Pacific/Efate', 'UTC+11:00'),
('Norfolk Island Time', 'Pacific/Norfolk', 'UTC+11:00'),
('Magadan Time', 'Asia/Magadan', 'UTC+11:00'),
('Kosrae Time', 'Pacific/Kosrae', 'UTC+11:00'),
('Sakhalin Time', 'Asia/Sakhalin', 'UTC+11:00'),
('New Caledonia Time', 'Pacific/Noumea', 'UTC+11:00'),
('Srednekolymsk Time', 'Asia/Srednekolymsk', 'UTC+11:00'),
('Solomon Islands Time', 'Pacific/Guadalcanal', 'UTC+11:00'),
('Lord Howe Standard Time', 'Australia/Lord_Howe', 'UTC+10:30'),
('Lord Howe Standard Time', 'Australia/LHI', 'UTC+10:30'),
('Australian Eastern Standard Time', 'Australia/Hobart', 'UTC+10:00'),
('Yap Time', 'Pacific/Yap', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Tasmania', 'UTC+10:00'),
('Papua New Guinea Time', 'Pacific/Port_Moresby', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/ACT', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Victoria', 'UTC+10:00'),
('Chuuk Time', 'Pacific/Chuuk', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Queensland', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Canberra', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Currie', 'UTC+10:00'),
('Chamorro Standard Time', 'Pacific/Guam', 'UTC+10:00'),
('Chuuk Time', 'Pacific/Truk', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/NSW', 'UTC+10:00'),
('Vladivostok Time', 'Asia/Vladivostok', 'UTC+10:00'),
('Chamorro Standard Time', 'Pacific/Saipan', 'UTC+10:00'),
('Dumont-dUrville Time', 'Antarctica/DumontDUrville', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Sydney', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Brisbane', 'UTC+10:00'),
('Ust-Nera Time', 'Asia/Ust-Nera', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Melbourne', 'UTC+10:00'),
('Australian Eastern Standard Time', 'Australia/Lindeman', 'UTC+10:00'),
('Central Standard Time (Australia)', 'Australia/North', 'UTC+09:30'),
('Central Standard Time (Australia)', 'Australia/Yancowinna', 'UTC+09:30'),
('Central Standard Time (Australia)', 'Australia/Adelaide', 'UTC+09:30'),
('Central Standard Time (Australia)', 'Australia/Broken_Hill', 'UTC+09:30'),
('Central Standard Time (Australia)', 'Australia/South', 'UTC+09:30'),
('Central Standard Time (Australia)', 'Australia/Darwin', 'UTC+09:30'),
('Palau Time', 'Pacific/Palau', 'UTC+09:00'),
('Yakutsk Time', 'Asia/Chita', 'UTC+09:00'),
('East Timor Time', 'Asia/Dili', 'UTC+09:00'),
('West Papua Time', 'Asia/Jayapura', 'UTC+09:00'),
('Yakutsk Time', 'Asia/Yakutsk', 'UTC+09:00'),
('Korea Standard Time', 'Asia/Pyongyang', 'UTC+09:00'),
('Korea Standard Time', 'ROK', 'UTC+09:00'),
('Korea Standard Time', 'Asia/Seoul', 'UTC+09:00'),
('Yakutsk Time', 'Asia/Khandyga', 'UTC+09:00'),
('Japan Standard Time', 'Japan', 'UTC+09:00'),
('Japan Standard Time', 'Asia/Tokyo', 'UTC+09:00'),
('Eucla Time', 'Australia/Eucla', 'UTC+08:45'),
('Malaysia Time', 'Asia/Kuching', 'UTC+08:00'),
('China Standard Time', 'Asia/Chungking', 'UTC+08:00'),
('Australian Western Standard Time', 'Australia/Perth', 'UTC+08:00'),
('Macau Time', 'Asia/Macao', 'UTC+08:00'),
('Macau Time', 'Asia/Macau', 'UTC+08:00'),
('Choibalsan Time', 'Asia/Choibalsan', 'UTC+08:00'),
('China Standard Time', 'Asia/Shanghai', 'UTC+08:00'),
('Casey Time', 'Antarctica/Casey', 'UTC+08:00'),
('Ulaanbaatar Time', 'Asia/Ulan_Bator', 'UTC+08:00'),
('China Standard Time', 'Asia/Chongqing', 'UTC+08:00'),
('Ulaanbaatar Time', 'Asia/Ulaanbaatar', 'UTC+08:00'),
('Taiwan Time', 'Asia/Taipei', 'UTC+08:00'),
('Philippine Standard Time', 'Asia/Manila', 'UTC+08:00'),
('China Standard Time', 'PRC', 'UTC+08:00'),
('Makassar Time', 'Asia/Ujung_Pandang', 'UTC+08:00'),
('China Standard Time', 'Asia/Harbin', 'UTC+08:00'),
('Singapore Time', 'Singapore', 'UTC+08:00'),
('Brunei Time', 'Asia/Brunei', 'UTC+08:00'),
('Australian Western Standard Time', 'Australia/West', 'UTC+08:00'),
('Hong Kong Time', 'Asia/Hong_Kong', 'UTC+08:00'),
('Makassar Time', 'Asia/Makassar', 'UTC+08:00'),
('Hong Kong Time', 'Hongkong', 'UTC+08:00'),
('Malaysia Time', 'Asia/Kuala_Lumpur', 'UTC+08:00'),
('Irkutsk Time', 'Asia/Irkutsk', 'UTC+08:00'),
('Singapore Time', 'Asia/Singapore', 'UTC+08:00'),
('Western Indonesian Time', 'Asia/Pontianak', 'UTC+07:00'),
('Indochina Time', 'Asia/Phnom_Penh', 'UTC+07:00'),
('Novosibirsk Time', 'Asia/Novosibirsk', 'UTC+07:00'),
('Davis Time', 'Antarctica/Davis', 'UTC+07:00'),
('Tomsk Time', 'Asia/Tomsk', 'UTC+07:00'),
('Western Indonesian Time', 'Asia/Jakarta', 'UTC+07:00'),
('Barnaul Time', 'Asia/Barnaul', 'UTC+07:00'),
('Christmas Island Time', 'Indian/Christmas', 'UTC+07:00'),
('Indochina Time', 'Asia/Ho_Chi_Minh', 'UTC+07:00'),
('Hovd Time', 'Asia/Hovd', 'UTC+07:00'),
('Indochina Time', 'Asia/Bangkok', 'UTC+07:00'),
('Indochina Time', 'Asia/Vientiane', 'UTC+07:00'),
('Kuznetsk Time', 'Asia/Novokuznetsk', 'UTC+07:00'),
('Krasnoyarsk Time', 'Asia/Krasnoyarsk', 'UTC+07:00'),
('Indochina Time', 'Asia/Saigon', 'UTC+07:00'),
('Myanmar Time', 'Asia/Yangon', 'UTC+06:30'),
('Myanmar Time', 'Asia/Rangoon', 'UTC+06:30'),
('Cocos Islands Time', 'Indian/Cocos', 'UTC+06:30'),
('Xinjiang Time', 'Asia/Kashgar', 'UTC+06:00'),
('Alma-Ata Time', 'Asia/Almaty', 'UTC+06:00'),
('Bangladesh Time', 'Asia/Dacca', 'UTC+06:00'),
('Omsk Time', 'Asia/Omsk', 'UTC+06:00'),
('Bangladesh Time', 'Asia/Dhaka', 'UTC+06:00'),
('Chagos Time', 'Indian/Chagos', 'UTC+06:00'),
('Qyzylorda Time', 'Asia/Qyzylorda', 'UTC+06:00'),
('Kyrgyzstan Time', 'Asia/Bishkek', 'UTC+06:00'),
('Vostok Time', 'Antarctica/Vostok', 'UTC+06:00'),
('Xinjiang Time', 'Asia/Urumqi', 'UTC+06:00'),
('Bhutan Time', 'Asia/Thimbu', 'UTC+06:00'),
('Bhutan Time', 'Asia/Thimphu', 'UTC+06:00'),
('Nepal Time', 'Asia/Kathmandu', 'UTC+05:45'),
('Nepal Time', 'Asia/Katmandu', 'UTC+05:45'),
('Indian Standard Time', 'Asia/Kolkata', 'UTC+05:30'),
('Sri Lanka Standard Time', 'Asia/Colombo', 'UTC+05:30'),
('Indian Standard Time', 'Asia/Calcutta', 'UTC+05:30'),
('Aqtau Time', 'Asia/Aqtau', 'UTC+05:00'),
('Samarkand Time', 'Asia/Samarkand', 'UTC+05:00'),
('Pakistan Standard Time', 'Asia/Karachi', 'UTC+05:00'),
('Yekaterinburg Time', 'Asia/Yekaterinburg', 'UTC+05:00'),
('Tajikistan Time', 'Asia/Dushanbe', 'UTC+05:00'),
('Maldives Time', 'Indian/Maldives', 'UTC+05:00'),
('Oral Time', 'Asia/Oral', 'UTC+05:00'),
('Uzbekistan Time', 'Asia/Tashkent', 'UTC+05:00'),
('Mawson Time', 'Antarctica/Mawson', 'UTC+05:00'),
('Aqtobe Time', 'Asia/Aqtobe', 'UTC+05:00'),
('Turkmenistan Time', 'Asia/Ashkhabad', 'UTC+05:00'),
('Turkmenistan Time', 'Asia/Ashgabat', 'UTC+05:00'),
('Atyrau Time', 'Asia/Atyrau', 'UTC+05:00'),
('Kerguelen Time', 'Indian/Kerguelen', 'UTC+05:00'),
('Iran Standard Time', 'Iran', 'UTC+04:30'),
('Iran Standard Time', 'Asia/Tehran', 'UTC+04:30'),
('Afghanistan Time', 'Asia/Kabul', 'UTC+04:30'),
('Armenia Time', 'Asia/Yerevan', 'UTC+04:00'),
('Gulf Standard Time', 'Asia/Dubai', 'UTC+04:00'),
('Reunion Time', 'Indian/Reunion', 'UTC+04:00'),
('Mauritius Time', 'Indian/Mauritius', 'UTC+04:00'),
('Saratov Time', 'Europe/Saratov', 'UTC+04:00'),
('Samara Time', 'Europe/Samara', 'UTC+04:00'),
('Seychelles Time', 'Indian/Mahe', 'UTC+04:00'),
('Azerbaijan Time', 'Asia/Baku', 'UTC+04:00'),
('Oman Standard Time', 'Asia/Muscat', 'UTC+04:00'),
('Volgograd Time', 'Europe/Volgograd', 'UTC+04:00'),
('Astrakhan Time', 'Europe/Astrakhan', 'UTC+04:00'),
('Georgia Time', 'Asia/Tbilisi', 'UTC+04:00'),
('Ulyanovsk Time', 'Europe/Ulyanovsk', 'UTC+04:00'),
('Arabian Standard Time', 'Asia/Aden', 'UTC+03:00'),
('East Africa Time', 'Africa/Nairobi', 'UTC+03:00'),
('Turkey Time', 'Europe/Istanbul', 'UTC+03:00'),
('Eastern European Time', 'Europe/Zaporozhye', 'UTC+03:00'),
('Israel Standard Time', 'Israel', 'UTC+03:00'),
('Comoro Time', 'Indian/Comoro', 'UTC+03:00'),
('Syowa Time', 'Antarctica/Syowa', 'UTC+03:00'),
('East Africa Time', 'Africa/Mogadishu', 'UTC+03:00'),
('Eastern European Time', 'Europe/Bucharest', 'UTC+03:00'),
('East Africa Time', 'Africa/Asmera', 'UTC+03:00'),
('Eastern European Time', 'Europe/Mariehamn', 'UTC+03:00'),
('Turkey Time', 'Asia/Istanbul', 'UTC+03:00'),
('Eastern European Time', 'Europe/Tiraspol', 'UTC+03:00'),
('Moscow Standard Time', 'Europe/Moscow', 'UTC+03:00'),
('Eastern European Time', 'Europe/Chisinau', 'UTC+03:00'),
('Eastern European Time', 'Europe/Helsinki', 'UTC+03:00'),
('Eastern European Time', 'Asia/Beirut', 'UTC+03:00'),
('Israel Standard Time', 'Asia/Tel_Aviv', 'UTC+03:00'),
('East Africa Time', 'Africa/Djibouti', 'UTC+03:00'),
('Moscow Time', 'Europe/Simferopol', 'UTC+03:00'),
('Eastern European Time', 'Europe/Sofia', 'UTC+03:00'),
('Eastern European Time', 'Asia/Gaza', 'UTC+03:00'),
('East Africa Time', 'Africa/Asmara', 'UTC+03:00'),
('Eastern European Time', 'Europe/Riga', 'UTC+03:00'),
('Arabian Standard Time', 'Asia/Baghdad', 'UTC+03:00'),
('Eastern European Time', 'Asia/Damascus', 'UTC+03:00'),
('East Africa Time', 'Africa/Dar_es_Salaam', 'UTC+03:00'),
('East Africa Time', 'Africa/Addis_Ababa', 'UTC+03:00'),
('Eastern European Time', 'Europe/Uzhgorod', 'UTC+03:00'),
('Israel Standard Time', 'Asia/Jerusalem', 'UTC+03:00'),
('Arabian Standard Time', 'Asia/Riyadh', 'UTC+03:00'),
('Arabian Standard Time', 'Asia/Kuwait', 'UTC+03:00'),
('Moscow Standard Time', 'Europe/Kirov', 'UTC+03:00'),
('East Africa Time', 'Africa/Kampala', 'UTC+03:00'),
('Eastern European Time', 'Europe/Minsk', 'UTC+03:00'),
('Arabian Standard Time', 'Asia/Qatar', 'UTC+03:00'),
('Eastern European Time', 'Europe/Kiev', 'UTC+03:00'),
('Arabian Standard Time', 'Asia/Bahrain', 'UTC+03:00'),
('Eastern European Time', 'Europe/Vilnius', 'UTC+03:00'),
('Eastern Africa Time', 'Indian/Antananarivo', 'UTC+03:00'),
('Eastern Africa Time', 'Indian/Mayotte', 'UTC+03:00'),
('Eastern European Time', 'Europe/Tallinn', 'UTC+03:00'),
('Eastern Africa Time', 'Africa/Juba', 'UTC+03:00'),
('Eastern European Time', 'Asia/Nicosia', 'UTC+03:00'),
('Eastern European Time', 'Asia/Famagusta', 'UTC+03:00'),
('Eastern European Time', 'Asia/Hebron', 'UTC+03:00'),
('Eastern European Time', 'Asia/Amman', 'UTC+03:00'),
('Eastern European Time', 'Europe/Nicosia', 'UTC+03:00'),
('Eastern European Time', 'Europe/Athens', 'UTC+03:00'),
('Central European Time', 'Africa/Cairo', 'UTC+02:00'),
('South African Standard Time', 'Africa/Mbabane', 'UTC+02:00'),
('Central European Time', 'Europe/Brussels', 'UTC+02:00'),
('Central European Time', 'Europe/Warsaw', 'UTC+02:00'),
('Central European Time', 'Europe/Luxembourg', 'UTC+02:00'),
('Central Africa Time', 'Africa/Kigali', 'UTC+02:00'),
('Libya Standard Time', 'Africa/Tripoli', 'UTC+02:00'),
('Eastern European Time', 'Europe/Kaliningrad', 'UTC+02:00'),
('Central Africa Time', 'Africa/Windhoek', 'UTC+02:00'),
('Central European Time', 'Europe/Malta', 'UTC+02:00'),
('Central European Time', 'Europe/Busingen', 'UTC+02:00'),
('Central European Time', 'Europe/Skopje', 'UTC+02:00'),
('Central European Time', 'Europe/Sarajevo', 'UTC+02:00'),
('Central European Time', 'Europe/Rome', 'UTC+02:00'),
('Central European Time', 'Europe/Zurich', 'UTC+02:00'),
('Central European Time', 'Europe/Gibraltar', 'UTC+02:00'),
('Central Africa Time', 'Africa/Lubumbashi', 'UTC+02:00'),
('Central European Time', 'Europe/Vaduz', 'UTC+02:00'),
('Central European Time', 'Europe/Ljubljana', 'UTC+02:00'),
('Central European Time', 'Europe/Berlin', 'UTC+02:00'),
('Central European Time', 'Europe/Stockholm', 'UTC+02:00'),
('Central European Time', 'Europe/Budapest', 'UTC+02:00'),
('Central European Time', 'Europe/Zagreb', 'UTC+02:00'),
('Central European Time', 'Europe/Paris', 'UTC+02:00'),
('Central European Time', 'Africa/Ceuta', 'UTC+02:00'),
('Central European Time', 'Europe/Prague', 'UTC+02:00'),
('Central European Time', 'Antarctica/Troll', 'UTC+02:00'),
('Central Africa Time', 'Africa/Gaborone', 'UTC+02:00'),
('Central European Time', 'Europe/Copenhagen', 'UTC+02:00'),
('Central European Time', 'Europe/Vienna', 'UTC+02:00'),
('Central European Time', 'Europe/Tirane', 'UTC+02:00'),
('Central European Time', 'Europe/Amsterdam', 'UTC+02:00'),
('South African Standard Time', 'Africa/Maputo', 'UTC+02:00'),
('Central European Time', 'Europe/San_Marino', 'UTC+02:00'),
('Central European Time', 'Europe/Andorra', 'UTC+02:00'),
('Central European Time', 'Europe/Oslo', 'UTC+02:00'),
('Central European Time', 'Europe/Podgorica', 'UTC+02:00'),
('Central Africa Time', 'Africa/Bujumbura', 'UTC+02:00'),
('Central European Time', 'Atlantic/Jan_Mayen', 'UTC+02:00'),
('South African Standard Time', 'Africa/Maseru', 'UTC+02:00'),
('Central European Time', 'Europe/Madrid', 'UTC+02:00'),
('South Africa Standard Time', 'Africa/Blantyre', 'UTC+02:00'),
('South Africa Standard Time', 'Africa/Lusaka', 'UTC+02:00'),
('South Africa Standard Time', 'Africa/Harare', 'UTC+02:00'),
('Central Africa Time', 'Africa/Khartoum', 'UTC+02:00'),
('South African Standard Time', 'Africa/Johannesburg', 'UTC+02:00'),
('Central European Time', 'Europe/Belgrade', 'UTC+02:00'),
('Central European Time', 'Europe/Bratislava', 'UTC+02:00'),
('Central European Time', 'Arctic/Longyearbyen', 'UTC+02:00'),
('Central European Time', 'Europe/Vatican', 'UTC+02:00'),
('Central European Time', 'Europe/Monaco', 'UTC+02:00'),
('Greenwich Mean Time', 'Europe/London', 'UTC+01:00'),
('Greenwich Mean Time', 'Europe/Jersey', 'UTC+01:00'),
('Greenwich Mean Time', 'Europe/Guernsey', 'UTC+01:00'),
('Greenwich Mean Time', 'Europe/Isle_of_Man', 'UTC+01:00'),
('Central European Time', 'Africa/Tunis', 'UTC+01:00'),
('West Africa Time', 'Africa/Malabo', 'UTC+01:00'),
('GMT/Irish Standard Time', 'GB-Eire', 'UTC+01:00'),
('West Africa Time', 'Africa/Lagos', 'UTC+01:00'),
('Central European Time', 'Africa/Algiers', 'UTC+01:00'),
('West Africa Time', 'Africa/Sao_Tome', 'UTC+01:00'),
('West Africa Time', 'Africa/Ndjamena', 'UTC+01:00'),
('Greenwich Mean Time', 'Atlantic/Faeroe', 'UTC+01:00'),
('Greenwich Mean Time', 'Atlantic/Faroe', 'UTC+01:00'),
('Irish Standard Time', 'Europe/Dublin', 'UTC+01:00'),
('West Africa Time', 'Africa/Libreville', 'UTC+01:00'),
('Western Sahara Standard Time', 'Africa/El_Aaiun', 'UTC+01:00'),
('West Africa Time', 'Africa/Douala', 'UTC+01:00'),
('West Africa Time', 'Africa/Brazzaville', 'UTC+01:00'),
('West Africa Time', 'Africa/Porto-Novo', 'UTC+01:00'),
('Madeira Time', 'Atlantic/Madeira', 'UTC+01:00'),
('Western European Time', 'Europe/Lisbon', 'UTC+01:00'),
('Canary Islands Time', 'Atlantic/Canary', 'UTC+01:00'),
('Western European Time', 'Africa/Casablanca', 'UTC+01:00'),
('Greenwich Mean Time', 'Europe/Belfast', 'UTC+01:00'),
('West Africa Time', 'Africa/Luanda', 'UTC+01:00'),
('West Africa Time', 'Africa/Kinshasa', 'UTC+01:00'),
('West Africa Time', 'Africa/Bangui', 'UTC+01:00'),
('West Africa Time', 'Africa/Niamey', 'UTC+01:00'),
('Greenwich Mean Time', 'GMT', 'UTC+00:00'),
('St. Helena Time', 'Atlantic/St_Helena', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Banjul', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Freetown', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Bamako', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Conakry', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Nouakchott', 'UTC+00:00'),
('Coordinated Universal Time', 'UTC', 'UTC+00:00'), -- default timezone
('Azores Standard Time', 'Atlantic/Azores', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Abidjan', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Accra', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Ouagadougou', 'UTC+00:00'),
('Greenwich Mean Time', 'Atlantic/Reykjavik', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Lome', 'UTC+00:00'),
('Greenland Mean Time', 'America/Danmarkshavn', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Dakar', 'UTC+00:00'),
('Greenland Mean Time', 'America/Scoresbysund', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Bissau', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Timbuktu', 'UTC+00:00'),
('Greenwich Mean Time', 'Africa/Monrovia', 'UTC+00:00'),
-- Across the Atlantic ocean
('Cape Verde Time', 'Atlantic/Cape_Verde', 'UTC-01:00'),
('South Georgia and the South Sandwich Islands Time', 'Atlantic/South_Georgia', 'UTC-02:00'),
('Fernando de Noronha Time', 'America/Noronha', 'UTC-02:00'),
('Greenland Standard Time', 'America/Godthab', 'UTC-02:00'),
('St. Pierre and Miquelon Standard Time', 'America/Miquelon', 'UTC-02:00'),
('Newfoundland Standard Time', 'Canada/Newfoundland', 'UTC-02:30'),
('Newfoundland Standard Time', 'America/St_Johns', 'UTC-02:30'),
('Argentina Standard Time', 'America/Rosario', 'UTC-03:00'),
('Atlantic Standard Time', 'America/Goose_Bay', 'UTC-03:00'),
('Brasilia Time', 'America/Bahia', 'UTC-03:00'),
('Argentina Standard Time', 'America/Jujuy', 'UTC-03:00'),
('Brasilia Time', 'America/Belem', 'UTC-03:00'),
('Thule Time', 'America/Thule', 'UTC-03:00'),
('Brasilia Time', 'America/Fortaleza', 'UTC-03:00'),
('Atlantic Standard Time', 'America/Glace_Bay', 'UTC-03:00'),
('Chile Standard Time', 'America/Punta_Arenas', 'UTC-03:00'),
('Palmer Time', 'Antarctica/Palmer', 'UTC-03:00'),
('Rothera Time', 'Antarctica/Rothera', 'UTC-03:00'),
('Atlantic Standard Time', 'America/Halifax', 'UTC-03:00'),
('Falkland Islands Time', 'Atlantic/Stanley', 'UTC-03:00'),
('Brasilia Time', 'America/Maceio', 'UTC-03:00'),
('Atlantic Standard Time', 'Atlantic/Bermuda', 'UTC-03:00'),
('Brasilia Time', 'America/Santarem', 'UTC-03:00'),
('Argentina Standard Time', 'America/Mendoza', 'UTC-03:00'),
('Atlantic Standard Time', 'America/Moncton', 'UTC-03:00'),
('Suriname Time', 'America/Paramaribo', 'UTC-03:00'),
('Argentina Standard Time', 'America/Buenos_Aires', 'UTC-03:00'),
('Brasilia Time', 'America/Recife', 'UTC-03:00'),
('Cayenne Time', 'America/Cayenne', 'UTC-03:00'),
('Argentina Standard Time', 'America/Jujuy', 'UTC-03:00'),
('Brasilia Time', 'America/Sao_Paulo', 'UTC-03:00'),
('Argentina Standard Time', 'America/Cordoba', 'UTC-03:00'),
('Argentina Standard Time', 'America/Catamarca', 'UTC-03:00'),
('Uruguay Time', 'America/Montevideo', 'UTC-03:00'),
('Brasilia Time', 'America/Araguaina', 'UTC-03:00'),
('Atlantic Standard Time', 'Canada/Atlantic', 'UTC-03:00'),
('Eastern Standard Time', 'America/Toronto', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Guadeloupe', 'UTC-04:00'),
('Venezuela Time', 'America/Caracas', 'UTC-04:00'),
('Atlantic Standard Time', 'America/St_Kitts', 'UTC-04:00'),
('Eastern Standard Time', 'America/New_York', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Grenada', 'UTC-04:00'),
('Amazonas Time', 'America/Boa_Vista', 'UTC-04:00'),
('Eastern Standard Time', 'America/Montreal', 'UTC-04:00'),
('Eastern Standard Time', 'America/Pangnirtung', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Virgin', 'UTC-04:00'),
('Amazonas Time', 'America/Campo_Grande', 'UTC-04:00'),
('Amazonas Time', 'America/Porto_Velho', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Tortola', 'UTC-04:00'),
('Eastern Standard Time', 'America/Detroit', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Lower_Princes', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Montserrat', 'UTC-04:00'),
('Atlantic Standard Time', 'America/St_Lucia', 'UTC-04:00'),
('Eastern Standard Time', 'America/Nipigon', 'UTC-04:00'),
('Atlantic Standard Time', 'America/St_Barthelemy', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Port-au-Prince', 'UTC-04:00'),
('Eastern Standard Time', 'Canada/Eastern', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Santo_Domingo', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Blanc-Sablon', 'UTC-04:00'),
('Eastern Standard Time', 'America/Thunder_Bay', 'UTC-04:00'),
('Bolivia Time', 'America/La_Paz', 'UTC-04:00'),
('Chile Standard Time', 'America/Santiago', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Aruba', 'UTC-04:00'),
('Eastern Standard Time', 'America/Nassau', 'UTC-04:00'),
('Paraguay Time', 'America/Asuncion', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Dominica', 'UTC-04:00'),
('Atlantic Standard Time', 'America/St_Vincent', 'UTC-04:00'),
('Eastern Standard Time', 'America/Iqaluit', 'UTC-04:00'),
('Eastern Standard Time', 'America/Indianapolis', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Antigua', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Kralendijk', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Port_of_Spain', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Puerto_Rico', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Martinique', 'UTC-04:00'),
('Guyana Time', 'America/Guyana', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Curacao', 'UTC-04:00'),
('Eastern Standard Time', 'America/Louisville', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Barbados', 'UTC-04:00'),
('Cuba Standard Time', 'America/Havana', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Anguilla', 'UTC-04:00'),
('Atlantic Standard Time', 'America/St_Thomas', 'UTC-04:00'),
('Eastern Standard Time', 'America/Fort_Wayne', 'UTC-04:00'),
('Amazonas Time', 'America/Manaus', 'UTC-04:00'),
('Cuba Standard Time', 'Cuba', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Grand_Turk', 'UTC-04:00'),
('Chile Standard Time', 'Chile/Continental', 'UTC-04:00'),
('Atlantic Standard Time', 'America/Marigot', 'UTC-04:00'),
('Amazonas Time', 'America/Cuiaba', 'UTC-04:00'),
('Central Standard Time', 'America/Winnipeg', 'UTC-05:00'),
('Central Standard Time', 'America/North_Dakota/New_Salem', 'UTC-05:00'),
('Central Standard Time', 'America/Merida', 'UTC-05:00'),
('Eastern Standard Time', 'Jamaica', 'UTC-05:00'),
('Acre Time', 'America/Rio_Branco', 'UTC-05:00'),
('Central Standard Time', 'America/Bahia_Banderas', 'UTC-05:00'),
('Peru Time', 'America/Lima', 'UTC-05:00'),
('Central Standard Time', 'America/Cancun', 'UTC-05:00'),
('Central Standard Time', 'Canada/Central', 'UTC-05:00'),
('Eastern Standard Time', 'America/Resolute', 'UTC-05:00'),
('Central Standard Time', 'America/Menominee', 'UTC-05:00'),
('Colombia Time', 'America/Bogota', 'UTC-05:00'),
('Central Standard Time', 'America/Knox_IN', 'UTC-05:00'),
('Central Standard Time', 'America/Matamoros', 'UTC-05:00'),
('Central Standard Time', 'America/Mexico_City', 'UTC-05:00'),
('Eastern Standard Time', 'America/Cayman', 'UTC-05:00'),
('Central Standard Time', 'America/North_Dakota/Center', 'UTC-05:00'),
('Central Standard Time', 'America/Coral_Harbour', 'UTC-05:00'),
('Central Standard Time', 'America/Atikokan', 'UTC-05:00'),
('Eastern Standard Time', 'America/Jamaica', 'UTC-05:00'),
('Central Standard Time', 'America/Monterrey', 'UTC-05:00'),
('Central Standard Time', 'America/North_Dakota/Beulah', 'UTC-05:00'),
('Central Standard Time', 'America/Rainy_River', 'UTC-05:00'),
('Central Standard Time', 'America/Rankin_Inlet', 'UTC-05:00'),
('Ecuador Time', 'America/Guayaquil', 'UTC-05:00'),
('Acre Time', 'America/Porto_Acre', 'UTC-05:00'),
('Amazonas Time', 'America/Eirunepe', 'UTC-05:00'),
('Central Standard Time', 'America/Chicago', 'UTC-05:00'), -- app timezone
('Central Standard Time', 'America/Panama', 'UTC-05:00'),
('Mountain Standard Time', 'America/Shiprock', 'UTC-06:00'),
('Central Standard Time', 'Canada/Saskatchewan', 'UTC-06:00'),
('Mountain Standard Time', 'America/Cambridge_Bay', 'UTC-06:00'),
('Mountain Standard Time', 'Canada/Mountain', 'UTC-06:00'),
('Mountain Standard Time', 'America/Edmonton', 'UTC-06:00'),
('Easter Island Time', 'Chile/EasterIsland', 'UTC-06:00'),
('Mountain Standard Time', 'America/Ojinaga', 'UTC-06:00'),
('Mountain Standard Time', 'America/Chihuahua', 'UTC-06:00'),
('Central Standard Time', 'America/Costa_Rica', 'UTC-06:00'),
('Mountain Standard Time', 'America/Boise', 'UTC-06:00'),
('Mountain Standard Time', 'America/Mazatlan', 'UTC-06:00'),
('Mountain Standard Time', 'America/Inuvik', 'UTC-06:00'),
('Central Standard Time', 'America/Swift_Current', 'UTC-06:00'),
('Mountain Standard Time', 'America/Yellowknife', 'UTC-06:00'),
('Galapagos Time', 'Pacific/Galapagos', 'UTC-06:00'),
('Mountain Standard Time', 'America/Denver', 'UTC-06:00'),
('Central Standard Time', 'America/Regina', 'UTC-06:00'),
('Easter Island Time', 'Pacific/Easter', 'UTC-06:00'),
('Central Standard Time', 'America/Tegucigalpa', 'UTC-06:00'),
('Central Standard Time', 'America/Managua', 'UTC-06:00'),
('Central Standard Time', 'America/Belize', 'UTC-06:00'),
('Central Standard Time', 'America/Guatemala', 'UTC-06:00'),
('Central Standard Time', 'America/El_Salvador', 'UTC-06:00'),
('Pacific Standard Time', 'America/Los_Angeles', 'UTC-07:00'),
('Pacific Standard Time', 'America/Fort_Nelson', 'UTC-07:00'),
('Pacific Standard Time', 'America/Whitehorse', 'UTC-07:00'),
('Mountain Standard Time', 'America/Phoenix', 'UTC-07:00'),
('Pacific Standard Time', 'America/Ensenada', 'UTC-07:00'),
('Pacific Standard Time', 'America/Vancouver', 'UTC-07:00'),
('Mountain Standard Time', 'America/Santa_Isabel', 'UTC-07:00'),
('Mountain Standard Time', 'America/Hermosillo', 'UTC-07:00'),
('Mountain Standard Time', 'America/Creston', 'UTC-07:00'),
('Pacific Standard Time', 'America/Tijuana', 'UTC-07:00'),
('Pacific Standard Time', 'America/Dawson', 'UTC-07:00'),
('Pacific Standard Time', 'Canada/Pacific', 'UTC-07:00'),
('Pacific Standard Time', 'America/Dawson_Creek', 'UTC-07:00'),
('Pacific Standard Time', 'Canada/Yukon', 'UTC-07:00'),
('Alaska Standard Time', 'America/Nome', 'UTC-08:00'),
('Alaska Standard Time', 'America/Anchorage', 'UTC-08:00'),
('Alaska Standard Time', 'America/Sitka', 'UTC-08:00'),
('Pitcairn Standard Time', 'Pacific/Pitcairn', 'UTC-08:00'),
('Alaska Standard Time', 'America/Yakutat', 'UTC-08:00'),
('Alaska Standard Time', 'America/Metlakatla', 'UTC-08:00'),
('Alaska Standard Time', 'America/Juneau', 'UTC-08:00'),
('Alaska Standard Time', 'America/Adak', 'UTC-09:00'),
('Alaska Standard Time', 'America/Atka', 'UTC-09:00'),
('Gambier Time', 'Pacific/Gambier', 'UTC-09:00'),
('Marquesas Time', 'Pacific/Marquesas', 'UTC-09:30'),
('Johnston Island Time', 'Pacific/Johnston', 'UTC-10:00'),
('Tahiti Time', 'Pacific/Tahiti', 'UTC-10:00'),
('Rarotonga Time', 'Pacific/Rarotonga', 'UTC-10:00'),
('Hawaii Standard Time', 'Pacific/Honolulu', 'UTC-10:00'),
('Midway Islands Time', 'Pacific/Midway', 'UTC-11:00'),
('Niue Time', 'Pacific/Niue', 'UTC-11:00'),
('Samoa Standard Time', 'Pacific/Samoa', 'UTC-11:00'),
('Samoa Standard Time', 'Pacific/Pago_Pago', 'UTC-11:00');

CREATE TABLE language (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL,
    local_name VARCHAR(32), -- name in local language
    iso_code CHAR(2) NOT NULL, -- ISO 639 alpha-2 codes
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id)
);

CREATE TABLE currency (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL, -- i.e: United States Dollar
    symbol VARCHAR(4) NOT NULL, -- i.e: $
    iso_code VARCHAR(3) NOT NULL, -- i.e: USD
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id)
);

CREATE TABLE country (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    short_name VARCHAR(64) UNIQUE NOT NULL,
    long_name VARCHAR(128) UNIQUE NOT NULL,
    local_name VARCHAR(64),
    alpha_2_code CHAR(2) UNIQUE NOT NULL, -- iso code 2 chars
    alpha_3_code CHAR(3) UNIQUE NOT NULL, -- iso code 3 chars
    numeric_code INT(3) UNIQUE , -- ie: 840
    capital VARCHAR(64), -- optional
    capital_id INT UNSIGNED,
    nationality_plural VARCHAR(32),
    nationality_singular VARCHAR(32),
    continent VARCHAR(16), -- i.e: Africa, Europe, North America, South America, Oceania, Asia, Middle East, Caribbean
    currency_id INT UNSIGNED,
    comment VARCHAR(255),
    location_id INT UNSIGNED, -- if normalized
    coordinates POINT NOT NULL SRID 4326, -- used for Geographic Information System (GIS)
    SPATIAL INDEX(coordinates),  -- enables efficient spatial queries
    latitude DECIMAL(11, 8), -- used for Haversine Formula
    longitude DECIMAL(11, 8), -- used for Haversine Formula
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id),
    FOREIGN KEY (location_id) REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE
    FOREIGN KEY (capital_id) REFERENCES city(id) ON UPDATE CASCADE ON DELETE SET NULL
    FOREIGN KEY (currency_id) REFERENCES currency(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE region (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    country_id INT UNSIGNED NOT NULL,
    location_id INT UNSIGNED,
    language_id INT UNSIGNED,
    name VARCHAR(64) NOT NULL,
    iso_code VARCHAR(8) NOT NULL, -- 3166-2 iso sub-division code
    coordinates POINT NOT NULL SRID 4326, -- used for Geographic Information System
    SPATIAL INDEX(coordinates), -- enables efficient spatial queries
    latitude DECIMAL(11, 8), -- used for Haversine Formula
    longitude DECIMAL(11, 8), -- used for Haversine Formula
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id),
    FOREIGN KEY (country_id) REFERENCES country(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Metropolitan area
-- Used to bundle cities of a suburban areas to a metropolitan area
CREATE TABLE metro (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    city_id INT, -- used as a REFERENCES to the city proper of the metro (optional)
    name VARCHAR(64) NOT NULL,
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id)
);

CREATE TABLE city (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    region_id INT UNSIGNED NOT NULL,
    metro_id INT UNSIGNED,
    timezone_id INT UNSIGNED,
    location_id INT UNSIGNED,
    name VARCHAR(64) NOT NULL,
    coordinates POINT NOT NULL SRID 4326, -- used for Geographic Information System
    SPATIAL INDEX(coordinates),  -- Enables efficient spatial queries
    latitude DECIMAL(11, 8), -- used for Haversine Formula
    longitude DECIMAL(11, 8), -- used for Haversine Formula
    status BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id),
    FOREIGN KEY (region_id) REFERENCES region(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (metro_id) REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (timezone_id) REFERENCES timezone(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- CREATE indices on foreign keys, UNIQUE and joined columns

-- Indices: location
CREATE SPATIAL INDEX idx_location_coordinates ON location(coordinates);
CREATE INDEX idx_location_lon ON location(longitude);
CREATE INDEX idx_location_lat ON location(latitude);

-- Indices: timezone
CREATE index idx_tz_name ON timezone(name);
CREATE index idx_tz_standard_name ON timezone(standard_time_name);
CREATE INDEX idx_tz_group_offset ON timezone(group_offset);

-- Indices: language
CREATE INDEX idx_language_name ON language(name);
CREATE INDEX idx_language_local_name ON language(local_name);
CREATE INDEX idx_language_code ON language(iso_code);

-- Indices: country
CREATE INDEX idx_country_short_name ON country(short_name);
CREATE INDEX idx_country_long_name ON country(long_name);
CREATE INDEX idx_country_local_name ON country(local_name);
CREATE INDEX idx_country_numeric_code ON country(numeric_code);
CREATE INDEX idx_country_location ON country(location_id);
CREATE INDEX idx_country_capital ON country(capital_id);
CREATE INDEX idx_country_currency ON currency(id);
CREATE INDEX idx_country_query ON country(short_name, location_id, alpha_2_code);
CREATE SPATIAL INDEX idx_country_coordinates ON country(coordinates);
CREATE INDEX idx_country_lon ON country(longitude);
CREATE INDEX idx_country_lat ON country(latitude);

-- Indices: region
CREATE INDEX idx_region_country ON region(country_id);
CREATE INDEX idx_region_language ON region(language_id);
CREATE INDEX idx_region_name ON region(name);
CREATE INDEX idx_region_iso_code ON region(iso_code);
CREATE INDEX idx_region_location ON region(location_id);
CREATE INDEX idx_region_query ON region(country_id, location_id, name);
CREATE SPATIAL INDEX idx_region_coordinates ON region(coordinates);
CREATE INDEX idx_region_lon ON region(longitude);
CREATE INDEX idx_region_lat ON region(latitude);

-- Indices: metro
CREATE INDEX idx_metro_city ON metro(city_id);
CREATE INDEX idx_metro_name ON metro(name);

-- Indices: city
CREATE INDEX idx_city_region ON city(region_id);
CREATE INDEX idx_city_metro ON city(metro_id);
CREATE INDEX idx_city_timezone ON city(timezone_id);
CREATE INDEX idx_city_location ON city(location_id);
CREATE INDEX idx_city_name ON city(name);
CREATE INDEX idx_city_query ON city(region_id, location_id, name, metro_id);
CREATE SPATIAL INDEX idx_city_coordinates ON city(coordinates);
CREATE INDEX idx_city_lon ON city(longitude);
CREATE INDEX idx_city_lat ON city(latitude);
