from py_modules.telegram.functions import Map 
from PIL import Image
TOKEN = '1861177956:AAGfxYGzvOlw4Fxwi4S6P_GOns-R_YwUFvA'
URL = 'https://qr-code-telegram-bot.herokuapp.com/'
URL_2 = 'https://potato-cashback.herokuapp.com'
URI = 'mongodb+srv://H_reugo:Nurmukhambetov@cluster0.vq2an.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

# SYSTEM INFO
TECHNICAL_STOP = False
groupChatId = 1654644284
bot_nickname = "KZcashback_bot"

# INFO ON CASHBACK
friend_money = 20
welcome_cashback_sum = 200
cashback = [0.06, 0.11]

# FRAUD CHECKER
MAX_BALANCE = 20000
NO_LIMIT = 100

# start - Разбуди меня... 😴
# qr - Скинуть фото QR 📋
# extract - Получить выписку 📄

TEMPLATE_MESSAGE = "Напиши /start чтобы разбудить меня... 😴"

items = [
	[ # HOUSEHOLD ITEMS
		Map({
			'name': "Бумага",
			'image': Image.open('./py_modules/telegram/images/items/household/toilet-paper.png'),
			'price': 700,
			'tag': "Туалетная бумага",
			'limit': 4,
		}),
		Map({
			'name': "Полотенце",
			'image': Image.open('./py_modules/telegram/images/items/household/towel.png'),
			'price': 1400,
			'tag': "Полотенце",
			'limit': 3,
		}),
		Map({
			'name': "Тапочки",
			'image': Image.open('./py_modules/telegram/images/items/household/slippers.png'),
			'price': 3000,
			'tag': "Тапочки",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Порошок",
			'image': Image.open('./py_modules/telegram/images/items/household/powder.png'),
			'price': 3000,
			'tag': "Порошок",
			'limit': 2,
		}),
		Map({
			'name': "Сковорода",
			'image': Image.open('./py_modules/telegram/images/items/household/pan.png'),
			'price': 10000,
			'tag': "Сковорода",
			'limit': 1,
		}),
	],
	[ # TOYS ITEMS
		Map({
			'name': "Кукла",
			'image': Image.open('./py_modules/telegram/images/items/toys/HKD207.jpg'),
			'price': 1680,
			'tag': "HKD207",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Грузовик",
			'image': Image.open('./py_modules/telegram/images/items/toys/1817-1.jpg'),
			'price': 1953,
			'tag': "1817-1",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Трактор",
			'image': Image.open('./py_modules/telegram/images/items/toys/1822-1.png'),
			'price': 1960,
			'tag': "1822-1",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Малыш",
			'image': Image.open('./py_modules/telegram/images/items/toys/LM2587.jpg'),
			'price': 2079,
			'tag': "LM2587",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Гоночная",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0633D.jpg'),
			'price': 2786,
			'tag': "M38-B0633D",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Вертолет",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0651.jpg'),
			'price': 4606,
			'tag': "M38-B0651",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Автобус",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0330.jpg'),
			'price': 4606,
			'tag': "M38-B0330",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Автофургон",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0566.png'),
			'price': 5166,
			'tag': "M38-B0566",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Ресторан",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0567.png'),
			'price': 5166,
			'tag': "M38-B0567",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Автозаправка",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0568.png'),
			'price': 5166,
			'tag': "M38-B0568",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Пожарная",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0625.png'),
			'price': 5166,
			'tag': "M38-B0625",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Машина",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0655.png'),
			'price': 6986,
			'tag': "M38-B0655",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Вертолет",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0656.png'),
			'price': 6986,
			'tag': "M38-B0656",
			'limit': NO_LIMIT,
		}),
		Map({
			'name': "Автомойка",
			'image': Image.open('./py_modules/telegram/images/items/toys/M38-B0759D.jpg'),
			'price': 7966,
			'tag': "M38-B0759D",
			'limit': NO_LIMIT,
		})
	]
]
empty_limit_arr = [[0] * len(x) for x in items]
tree = Map({
	'menu': {
		'text': "Привет! 😊 Скинь мне QR чека с покупками 📋, и получите от меня КЕШБЭК до 11% 💰❗️❗️❗️",
		'buttons': [
			[
				{
					'text': "Как это работает? 🤓",
					'callback': "сonditions",
				}
			],
			[
				{
					'text': "Мой кабинет 🗄",
					'callback': "profile",
				}
			],
			[
				{
					'text': "Скинуть QR чека 📋",
					'callback': "cashback_photo",
				}
			],
			[
				{
					'text': "МАГАЗИН 🛍",
					'callback': "list_sections",
				}
			],
		],
	},
	'cashback_photo': {
		'wrong_format': "Неправильный формат ввода",
		'qr_not_found': "QR не найден. Попробуйте снова",
		'wrong_qr': "QR недействителен",

		'text': "Получите от Продавца QR код чека. И скиньте фото QR мне 😁!",
		'result': "Дата: {}\nСумма: {}₸\nНачислен кешбэк: {}%\nКешбэк: {}₸",
		'buttons': [
			[
				{
					'text': "Подтвердить ✅",
					'callback': "cashback_photo_finish?{},{}",
				}
			],
			[
				{
					'text': "Сделать новое фото QR",
					'callback': "cashback_photo_cancel?cashback_photo,{}",
				}
			],
			[
				{
					'text': "Назад в меню 🏘",
					'callback': "cashback_photo_cancel?menu,{}",
				}
			]
		]
	},
	'share': {
		'image': Image.open('./py_modules/telegram/images/get_nickname_intro.jpg'),
		'text': "1. Пригласи друзей 👬 и получи кешбэк {}₸ 💰 за каждого!\n2. Скинь боту 🤖 контакты ваших друзей.\n3. Как только друг скачает бота, твой кешбэк зачислят на счет!".format(friend_money),
		'buttons': [
			[
				{
					'text': "Написать боту контакты друзей! 👬",
					'callback': "get_nicknames",
				}
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "profile",
				}
			],
		],
	},
	'get_nicknames': {
		'user_already_joined': "<strong>Ваш друг {} уже подписан на бота</strong>",
		'user_is_written': "<strong>Ваш друг {} уже записан у вас</strong>",
	
		'image': Image.open('./py_modules/telegram/images/get_nickname_instruction.jpg'),
		'text': "1. Нажми на значок скрепочки «📎» и выбери «контакты»\n2. Выбери друга для приглашения\n3. Бот запишет всех кого ты собираешься пригласить\n4. Как только твои друзья из списка подпишутся, кешбэк твой!\n\nСПИСОК ДРУЗЕЙ ДЛЯ ПОДПИСКИ",
		'buttons': [
			[
				{
					'text': "Готово ✅",
					'callback': "menu",
				},
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "share",
				}
			],
		],
	},
	'profile': {
		'text': "Остаток: {}₸\nДата: {}\nИмя: {}\nТелефон: {}",
		'buttons': [
			[
				{
					'text': "Выписка 📄",
					'callback': "extract",
				}
			],
			[
				{
					'text': "Поменять профиль 🛠",
					'callback': "register",
				}
			],
			[
				{
					'text': "Пригласи друга 👬 за кешбэк!",
					'callback': "share",
				}
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "menu",
				}
			],
		]
	},
	'extract': {
		'buttons': [
			[
				{
					'text': "Назад 🏘",
					'callback': "menu",
				}
			],
		]
	},
	'register': {
		'choose_name': "Давайте заполним ваши контакты. Как вас зовут 😉?",
		'get_telephone': "Пожалуйста, чтобы завершить регистрацию нажмите на кнопку <strong>«Продолжить»</strong>.",
		'check_info': "Проверьте все ли правильно?",
		'welcome_casback': "Поздравляю 🎉🥳! Вам начислен welcome кешбэк {}₸! 💰".format(welcome_cashback_sum),
		'previous_cashbacks': "Начислены предыдущие кешбэки в размере {}₸! 💰",

		'buttons': [
			[
				{
					'text': "Да ✅",
					'callback': "register_complete",
				},
				{
					'text': "Нет 🚫",
					'callback': "register",
				}
			],
		],
	},
	'faq': {
		'text': 'В : Бот написал, что QR недействителен, что делать?\n\nО : Проверьте четкость фотографии QR. Попросите помощи у Продавца или свяжитесь с оператором.\n\n\nВ : Я хочу вывести Кешбэк на свою банковскую карточку, как это сделать?\n\nО : На текущий момент Кешбэк нельзя вывести в качестве денежных средств на банковскую карточку.\n\n\nВ : Я написала боту ник (@username) своего друга, однако не получила Кешбэк. Что делать?\n\nО : Проверьте <strong>наличие и корректность</strong> написания @username, а также убедитесь в том что друг действительно присоединился к боту в телеграмме.',
		'buttons': [
			[
				{
					'text': "Задать вопрос оператору 📞",
					'callback': "ask_question",
				}
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "сonditions",
				}
			],
		]
	},
	'ask_question': {
		'text': 'Напишите нашему оператору @H_reugo 📞, он вам обязательно ответит 👨‍💻',
		'buttons': [
			[
				{
					'text': 'Назад 🏘',
					'callback': 'faq',
				}
			]
		]
	},
	'сonditions': {
		'image': Image.open('./py_modules/telegram/images/how_to_work.png'),
		'text': "1. Делай покупки у наших ПАРТНЕРОВ\n2. Скинь QR ЧЕК на покупки от Продавца\n3. Получи до 11% кешбэка на счет в Личном Кабинете\n4. Обменяй КЕШБЭК на ПОДАРКИ",
		'buttons': [
			[
				{
					'text': "Список партнеров 🏪",
					'callback': "list_partners",
				},
			],
			[
				{
					'text': "МАГАЗИН 🛍",
					'callback': "list_sections",
				}
			],
			[
				{
					'text': "Задать вопрос 📞",
					'callback': "faq",
				}
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "menu",
				}
			],
		]
	},
	'list_partners': {
		'text': "СПИСОК ПАРТНЕРОВ\n\n1. ИП \"Сулейман\" Рыскулбекова 28/5, ЖК \"Байтал\"",
		'buttons': [
			[
				{
					'text': "Назад 🏘",
					'callback': "сonditions",
				}
			],
		]
	},
	'list_sections': {
		'text': "Выберите категорию товаров",
		'buttons': [
			[
				{
					'text': "Игрушки",
					'callback': "list_gifts?0,1",
				}
			],
			[
				{
					'text': "Товары для дома",
					'callback': "list_gifts?0,0",
				}
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "menu",
				}
			]
		]
	},
	'list_gifts': {
		'buttons': [
			[
				{
					'text': "Цена: {}₸",
					'callback': "list_gifts?{},{}",
				}
			],
			[
				{
					'text': "<<",
					'callback': "list_gifts?{},{}",
				},
				{
					"text": "Хочу это!",
					'callback': "buy_gift?{},{}",
				},
				{
					'text': ">>",
					'callback': "list_gifts?{},{}",
				}
			],
			[
				{
					'text': "{} из {}",
					'callback': "list_gifts?{},{}",
				},
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "list_sections",
				}
			],
		]
	},
	'buy_gift': {
		'text': "КУПИТЬ {} ЗА {}₸?\n\nОстаток: {}₸\nДата: {}\nИмя: {}\nТелефон: {}",
		'buttons': [
			[
				{
					'text': "Хочу это!",
					'callback': "user_buy?{},{}",
				}
			],
			[
				{
					'text': "Назад 🏘",
					'callback': "list_gifts?0,{}"
				},
			],
		]
	},
	'user_buy': {
		'not_enough': "Упс ☹️, у вас не хватает баланса для покупки...",
		'limit_exceeded': "Извините, но покупка этого товара сейчас недоступна.",
		'text': "Отличный выбор 🤩! Наш оператор свяжется с вами 📞 для уточнения деталей",
		'buttons': [
			[
				{
					'text': "Назад 🏘",
					'callback': "menu",
				}
			],
		]
	},
	'confirmation': {
		'text': 'Артикул игрушки: <strong>{}</strong>\nПодтвердите пользователя @{}\n\nОстаток: {}₸\nИмя: {}\nТелефон: {}',
		'buttons': [
			[
				{
					'text': 'Одобрить ✅',
					'callback': 'confirmed?yes,{},{},{}',				
				},
				{
					'text': 'Отвергнуть ❌',
					'callback': 'confirmed?no,{},{},{}',
				}
			]
		]
	},
	'notification': {
		'stop': "Извините, идут технические работы",

		'product_warning': "Извините, но покупка этого товара сейчас недоступна. Ваши деньги возращены на счет",
		'product_success': "Твой заказ успешно подтверждён 🎉🥳! Ждите звонка нашего курьера 📞! До свидания! 👋",

		'client_info': "Артикул товара: <strong>{}</strong>\nПользователь @{} был {}\n\nОстаток: {}₸\nИмя: {}\nТелефон: {}",
		'not_registered': "Заполните ваши контакты в Личном кабинете",

		'balance_increase': "Ура! 🎉🥳! На ваш счет добавилось {}₸! 💰",
		'friend_join': "Ваш друг {} подписался на бота 👬! На ваш счет добавилось {}₸! 💰",

		'fraud_detect': "Произошла ошибка, достигнут лимит начисления кешбэка."
	},

	'operations': {
		'photo': "кешбэк",
		'back': "возврат",
		'register': "welcome",
	},
})

#    ДАТА    |   СУММА  | ОПЕРАЦИИ
# ===========|==========|=============
# 28/05/2021 | +123₸ | Обдобрит чек