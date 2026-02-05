from django.db import models

# Create your models here.
class Table(models.Model):
    table_number=models.PositiveBigIntegerField(unique=True)
    capacity=models.PositiveBigIntegerField(default=4)
    status=models.CharField(max_length=20,
    choices=[
        ('available','Available'),
        ('occupied','Occupied'),
        ('reserved','Reserved')
    ],
    default='available'
    )

    def __str__(self):
        return f"Table{self.table_number}"

class MenuCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name=models.CharField(max_length=200)
    Category=models.ForeignKey(MenuCategory,on_delete=models.CASCADE,related_name="items")
    price=models.DecimalField(max_digits=8,decimal_places=2,)
    availability=models.BooleanField(default=True)
    image=models.ImageField(upload_to="menu_images/",blank=True,null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    Status_choice=[
        ("PENDING","pending"),
        ("SERVED","served"),
        ("BILLED","billed"),
    ]
    table=models.ForeignKey(Table,on_delete=models.CASCADE,related_name="orders")
    status=models.CharField(max_length=10,choices=Status_choice,default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order{self.id}-Table{self.table.table_number}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    menu_item=models.ForeignKey(MenuItem,on_delete=models.PROTECT)
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(max_digits=8,decimal_places=2,)

    def save(self,*args ,**kwargs):
        self.price=self.menu_item.price*self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.menu_item.name} {self.quantity}(Order{self.order.id})"

class Bill(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE,related_name="bill")
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    discount=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    final_amount=models.DecimalField(max_digits=10,decimal_places=2)
    generated_at=models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        self.final_amount=max(self.total_amount - (self.total_amount * self.discount/100),)
        super().save(*args,**kwargs)



