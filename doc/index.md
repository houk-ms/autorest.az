# CLI Code-Gen Command Interface Use Cases


## 1. Command Group

### 1.1 Combine command groups
```
az group1 cmd1*
az group2 cmd2*
==>
az group3 cmd1*
az group3 cmd2*
```

### 1.2 Split command groups
```
az group3 cmd1*
az group3 cmd2*
==>
az group1 cmd1*
az group2 cmd2*
```

### 1.3 Rename command groups

#### 1.3.1 Single-layer
```
az group1 cmd*
==>
az group2 cmd*
```

#### 1.3.2 Multiple-layers
```
az group1 sub-group1 cmd*
==>
az group2 sub-group2 cmd*
```

### 1.4 Add command group

#### 1.4.1 Single-layer
```
az group cmd*
==>
az group [add-group] cmd*
az [add-group] group cmd*
```

#### 1.4.2 Multiple-layers
```
az group cmd*
==>
az group [add-group1] [add-group2] cmd*
az [add-group1] [add-group2] group cmd*
az [add-group1] group [add-group2] cmd*
```

### 1.5 Remove command group

#### 1.5.1 Single-layer
```
az group sub-group cmd*
==>
az sub-group cmd*
az group cmd*
```

#### 1.5.1 Multiple-layers
```
az group sub-group1 sub-group2 cmd*
==>
az group cmd*
az sub-group1 cmd*
az sub-group2 cmd*
```


## 2. Command

### 2.1 Rename command
```
az group sub-group cmd1
==>
az group sub-group cmd2
```

### 2.2 Remove command
```
az group sub-group cmd1
az group sub-group cmd2
==>
az group sub-group cmd1
```

### 2.3 Move command

#### 2.3.1 Between layers
```
az group sub-group cmd1
==>
az group cmd1
```

#### 2.3.2 Between command groups
```
az group sub-group1 cmd1
==>
az group sub-group2 cmd1
```

#### 2.3.3 Between layers and rename
```
az group sub-group cmd1
==>
az group cmd2
```

#### 2.3.4 Between command groups and rename
```
az group sub-group1 cmd1
==>
az group sub-group2 cmd2
```


## 3. Parameter

### 3.1 Rename parameter
```
az cmd --param1
==>
az cmd --param2
```

### 3.2 Remove parameter
```
az cmd --param1 --param2
==>
az cmd --param1
```

### 3.3 Add parameter
```
az cmd --param1
==>
az cmd --param1 --param2
```

### 3.4 Add parameter alias
```
az cmd --param1
==>
az cmd --param1/--param2
```

### 3.5 Required/optional
```
--param           : description
==>
--param [Required]: description
```
```
--param [Required]: description
==>
--param           : description
```


## 4. Description
### 4.1 command group

#### 4.1.1 Help message
```
az group:   description1
==>
az group:   description2
```
#### 4.1.2 Preview/Experimental tag
```
az group:   description
==>
az group [Preview]:   description
```

### 4.2 command

#### 4.2.1 Help message
```
az group cmd:   description1
==>
az group cmd:   description2
```

#### 4.2.2 Preview/Experimental tag
```
az group               :   description
==>
az group [Preview]     :   description
az group [Experimental]:   description
```

#### 4.2.3 Example
```
az group cmd
==>
az group cmd
Examples
    example_description
        example_command
```
```
az group cmd
==>
az group cmd
Examples
    example_description1
        example_command1
    example_description2
        example_command2
```

### 4.3 parameter

#### 4.3.1 Help message
```
--param1:   description1
==>
--param1:   description2
```

#### 4.3.2 Preview/Experimental tag
```
--param1               :   description
==>
--param1 [Preview]     :   description
--param1 [Experimental]:   description
```