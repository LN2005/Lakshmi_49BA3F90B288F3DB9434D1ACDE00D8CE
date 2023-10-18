def linearSearchProduct(productList, targetproduct):
  indices = []
  
  for index, product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)

  return indices
  
#example usage:
products = ['shoes', 'boots', 'Half sleeve shirts', "full leg pants", "sarees", "socks"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)

      