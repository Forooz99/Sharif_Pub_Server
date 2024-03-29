# سرور شریف‌پاب
- وب‌سایت شریف‌پاب محلی برای به اشتراک‌گذاری نشریه‌های دانشجویی است. ناشران با داشتن کد ناشر وارد حساب کاربری خود می‌شوند و در آنجا می‌توانند اطلاعات نشریه و برخی از اطلاعات کاربری را تغییر دهند، شماره‌ی جدید نشریه را روی سایت قرار دهند و یا شماره‌های قبلی را ویرایش یا حذف کنند. خوانندگان هم می‌توانند برای خود حساب کاربری جدید بسازند و نشریه‌ها و شماره‌های مورد علاقه خود را ذخیره کنند و با نام خود برای شماره‌ها نظر بدهند، همچنین می‌توانند اطلاعات خود را در پروفایل‌شان تغییر دهند. کاربران آزاد هم می‌توانند با عضو شدن در خبرنامه ما از آخرین شماره‌های منتشرشده مطلع شوند. در صفحه خانه هم نشریه‌های موجود نشان داده می‌شوند که با کلیک بر روی هر نشریه می‌توان لیستی از شماره‌های آن نشریه را دید.
- این مخزن کدهای سمت سرور شریف‌پاب را که با جنگو نوشته شده است را دارد، همچنین از دیتابیس ‌postgresql برای ذخیره دیتاها استفاده شده است.

# مستندات سرور
- در این پروژه که با جنگو نوشته شده است با توجه به منطق برنامه از دو اپ زیر استفاده شده است:
    اپ user: برای مدیریت کاربران که یک مدل پایه برای احراز هویت دارد (CustomUser) و دو مدل اصلی برنامه Reader, Publisher که از CustomUser ارث‌بری کرده‌اند و یک سری ویژگی‌های اضافی مخصوص به خود را نیز دارند.فیلد نام کاربری هم ایمیل کاربران و احراز هویت با ایمیل و گذرواژه انجام می‌شود. خوانندگان می‌توانند بدون ایجاد حساب کاربری هم نشریه‌ها را مشاهده کنند و شماره‌ها را بخوانند. در صورت ایجاد حساب کاربری می‌توانند نشریه‌های مورد علاقه و شماره‌های خوانده شده را ذخیره کنند و با نام کاربری خود کامنت بگذارند. همچنین پروفایل مخصوص خود را خواهند داشت که می‌توانند آواتار و نام کاربری و ایمیل و گذرواژه خود را عوض کنند. ناشرها باید به پروفایل از پیش تعریف‌شده خود که اطلاعاتشان از سمت دانشگاه تایید شده است وارد شوند و قابلیت ثبت‌نام ندارند. همچنین ناشرین هم قابلیت تغییر برخی از ویژگی‌های خود را دارند.
    همچنین برای هر کدام از کاربران api مخصوص به خود را دارند که عملیات اصلی CRUD روی مدل‌هایشان انجام می‌شود. ReadersAPI برای گرفتن اطلاعات کل خوانندگان (GET) و ساخت یک خواننده جدید است. ReadersByIdAPI هم برای عملیات آپدیت و حذف خواننده موجود است. عملیات Login, Signup, Logout هم ویوهای مخصوص به خود را دارند.
    اپ journal: برای مدیریت نشریات و شماره‌هایی که ناشران اجازه انتشار آن را در وب‌سایت دارند. ناشرین در پروفایل خود می‌توانند شماره‌های جدید نشریه‌شان را منتشر کنند و کامنت‌ها را ببینند و به آنها پاسخ دهند و تعداد لایک‌ها را رصد کنند. در این اپ هم دوتا مدل ‌journal, volume تعریف شده که ژورنال با کلید اصلی نام‌شان تعریف می‌شوند و شماره‌ها نیز موقع تعریف باید حتما ژورنال خود را تعیین کنند.
    برای نشریه و شماره هم به ترتیب JournalsAPI, VolumesAPI تعریف شده که عملیات اصلی ایجاد و آپدیت و حذف نشریه و ژورنال انجام می‌شود.
  - برای api ها هم از معماری rest استفاده شده و ‌url‌ها به صورت زیر تعریف شده اند:
  - api/v1/users/readers
  - api/v1/users/publishers
  - api/v1/users/readers/<str:pk>
  - api/v1/users/publishers/<str:pk>
  - api/v1/users/signup
  - api/v1/users/login
  - api/v1/users/logout
  - api/v1/journals
  - api/v1/journals/<str:pk>
  - api/v1/journals/volumes
  - api/v1/journals/volumes/<slug:pk>
   
  - برای ران کردن لوکال پروژه هم از ‍دستور زیر استفاده می‌کنیم:
##### `python manage.py runserver`

# مستندات زیرساخت
داکرایز بک اند به دو حالت development و production صورت گرفته است.

فایل های dockerfile و docker-compose برای حالت development هستند که یک کانتینر پایگاه داده و یک کانتینر برای سرور جنگو ساخته میشود و برای توسعه قابل استفاده است. کافی است دستور زیر را اجرا کنیم.
### `docker-compose -f docker-compose.yml build`

فایل های dockerfile.prof و docker-compose.prod برای حالت production هستند. در این حالت از gunicorn و nginx نیز استفاده میشود. کانتینر ها از طریق شبکه داخلی داکر با هم ارتباط دارند.
### `docker-compose -f docker-compose.prod.yml build`

