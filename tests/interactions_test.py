from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DropPage, DraggablePage


class TestInteraction:
    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectPage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, "no elements were selected"

    class TestResizablePage:

        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '380px') == max_box, "maximum size not equal to 500px"
            assert ('150px', '150px') == min_box, "maximum size not equal to 150px"
            assert min_resize != max_resize, "resizable has not been changed"

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DropPage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'the element has not been dropped'

        def test_accept_droppable(self, driver):
            droppable_page = DropPage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here!', 'the dropped element has not been dropped'
            assert accept == 'Dropped!', "the dropped element has not been dropped "

        def test_prevent_propogation_droppbale(self, driver):
            droppable_page = DropPage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'the dropped element has not been dropped '
            assert not_greedy_inner == 'Dropped!', "the dropped element has not been dropped "
            assert greedy == 'Outer droppable!', "the dropped element has not been dropped "
            assert greedy_inner == 'Dropped!', "the dropped element has not been dropped "

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DropPage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_dropable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_dropable('will_not')
            assert will_after_move != will_after_revert, 'the elements has not revert'
            assert not_will_after_move == not_will_after_revert, 'the elements has not revert'

    class TestDraggablePage:

        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "the position of has not been changet"

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x,left_x = draggable_page.axis_restricted_x('right')
            top_y,left_y = draggable_page.axis_restricted_y('down')
            assert top_x != left_x, 'the axis has not been changes'
            assert top_y != left_y, 'the axis has not been changes'


