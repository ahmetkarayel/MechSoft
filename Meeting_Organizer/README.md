<h1 align="center">Meeting Organizer</h1>

### Proje Tanımı
* Müşteriler ile yapılacak toplantıların kaydedilebileceği, güncellenebileceği ve silinebileceği bir tek sayfa uygulaması.

#### Yapılacaklar
> * Toplantı Kayıt Formu 
> * Toplantı Güncelleme Formu
> * Toplantı Listesi
> * WEB API Backend

---

* Projenin backend tarafını "Flask" ve "Postgresql" kullanarak gerçekleştirdim.

---

<h2 align="center"> Proje Tanıtımı </h2>

* "Toplantılar" için gerekli alanlardan oluşan SQL tablosunu oluşturuyorum.
>> ![image](https://user-images.githubusercontent.com/42919340/189505917-b567c41c-7a98-4664-89ea-5feb46a9b9af.png)

* Projenin görüntüsü bu şekilde;
>> ![AnaSayfa_1](https://user-images.githubusercontent.com/42919340/189505980-a9eb07bb-8530-442c-bbbd-951322829397.png)

Sol tarafta toplantı ekleme formu, sağ tarafta ise eklenen toplantıların listesi ve mevcut toplantılar için "Düzenle" ve "Sil" özellikleri aktif. 

* Bir toplantı eklemek istersek;
>> ![ToplantıEkleme](https://user-images.githubusercontent.com/42919340/189506034-68d217ea-51b6-4de2-bcbd-239d4f6d8916.png)

"Toplantı Kayıt Formu" üzerinden toplantı detaylarını kaydediyorum.

>> ![ToplantıEklendi](https://user-images.githubusercontent.com/42919340/189506059-31c891ed-7f3e-4361-8b9a-7c99c88a784f.png)

Yeni toplantımız başarılı bir şekilde eklendi.

* Eklediğimiz bir toplantının bilgilerini "Düzenle" seçeneği ile değiştirmek istersek;
>>> ![ToplantıDüzenleme](https://user-images.githubusercontent.com/42919340/189506149-88a4f99a-3311-4446-8787-25854fc0c5d7.png)
>>> ![ToplantıDüzenleme_2](https://user-images.githubusercontent.com/42919340/189506158-1d7f694e-691e-463a-bd3a-f1594ee3f223.png)
>>> ![ToplantıDüzenlendi](https://user-images.githubusercontent.com/42919340/189506159-fff918f8-a1b7-471b-9ebe-fc7394bdb802.png)

"Veri Bilimi" konulu toplantıyı "Python ile Backend" konulu olarak ve ileri bir tarihe erteledik. 

Yaptığımız tüm değişiklikler "postgresql" üzerinde de gerçekleştiriyor. Güncellediğimiz toplantıya bakalım;
>> ![pg_ToplantıEklendi](https://user-images.githubusercontent.com/42919340/189506206-a8a8209d-ac71-4ee2-b79b-c4399c2b7ed9.png)

* İlgili toplantıyı "Sil" butonu ile silmek istersek;
>>  ![ToplantıSilme](https://user-images.githubusercontent.com/42919340/189506226-d58fa0a9-e6e0-45ee-838f-e613ee9ec9fc.png)
>> ![ToplantıSilindi](https://user-images.githubusercontent.com/42919340/189506229-75026407-b2e2-4940-aaf5-59121b3d5978.png)

Toplantımızı başarılı bir şekilde sildik.








