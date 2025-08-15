def test_datatype():
    my_list=[12,45,56,78,"Hello"]
    print("i want to check value with index number")
    my_list.append("Anand Rawat")


    assert my_list[0]==12

    print("want to add name is existing list")
    assert my_list[-1]=="Anand Rawat"

    print("remove value with index number")

    my_list.remove(12)
    assert 12 not in my_list
    assert my_list==[45,56,78,'Hello','Anand Rawat']

    ashu=my_list.pop(1)

    assert ashu==56
    assert my_list==[45, 78, 'Hello', 'Anand Rawat']
