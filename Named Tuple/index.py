from collections import namedtuple

blog = namedtuple("Blog", ["site_name", "site_url", "site_twitter"])

print(blog)

sudanicoder = blog("SudaniCoder", "https://sudanicoder.pythonanywhere.com/", "@WIZOMERTHEBRO")

print(sudanicoder)
print(f"\n{sudanicoder.site_name}")

print(f"\n{sudanicoder.site_url}")

print(f"\n{sudanicoder.site_twitter}")
